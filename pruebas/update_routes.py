import re

def update_routes(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Import Form, json, os if not exists
    if "import json" not in content:
        content = content.replace("import fitz", "import fitz\nimport json\nimport os")
    if "Form" not in content:
        content = content.replace("BackgroundTasks", "BackgroundTasks, Form")

    # Reemplazar el bloque pre_validate_proposal
    pattern = re.compile(r'@router\.post\("/pre-validate-proposal"\).*?@router\.post\("/analyze-proposal-phi3"\)', re.DOTALL)
    
    new_code = '''# Asegurar que existe el directorio de drafts
DRAFTS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "drafts")
os.makedirs(DRAFTS_DIR, exist_ok=True)

@router.post("/pre-validate-proposal")
async def pre_validate_proposal(user_id: str = Form(...), file: UploadFile = File(...)):
    """
    Realiza una validación RÁPIDA y GUARDA un borrador local.
    """
    try:
        filename_lower = file.filename.lower()
        if not filename_lower.endswith(('.pdf', '.md', '.txt')):
            raise HTTPException(status_code=400, detail="El archivo debe ser PDF, MD o TXT")
            
        file_bytes = await file.read()
        full_text = ""
        if filename_lower.endswith('.pdf'):
            doc = fitz.open(stream=file_bytes, filetype="pdf")
            full_text = pymupdf4llm.to_markdown(doc)
        else:
            full_text = file_bytes.decode('utf-8')
                    
        if not full_text:
            raise HTTPException(status_code=400, detail="No se pudo extraer texto del documento.")

        if nlp_service.detect_prompt_injection(full_text):
            raise HTTPException(status_code=403, detail="ALERTA: Se detectó un intento de inyección de prompt.")

        clean_text = nlp_service.strip_structure(full_text)
        clean_text = nlp_service.normalize_homoglyphs(clean_text)
        safe_text = nlp_service.anonymize_pii(clean_text)

        chunks = nlp_service.chunk_text(safe_text)
        embeddings = nlp_service.vectorize(chunks)
        
        if not embeddings:
            raise HTTPException(status_code=400, detail="El documento no tiene contenido suficiente.")
        
        query_subset = embeddings[:5] if len(embeddings) > 5 else embeddings
        search_results = chroma_service.search_similar_multi(query_embeddings=query_subset, n_results=3)
        
        max_similitud_pct = 0.0
        similar_projects = []
        if search_results and "documents" in search_results and search_results["documents"]:
            grouped_projects = {}
            for q_idx in range(len(search_results["documents"])):
                docs = search_results["documents"][q_idx]
                metas = search_results["metadatas"][q_idx]
                distances = search_results["distances"][q_idx] if "distances" in search_results else [0]*len(docs)
                
                for doc, meta, dist in zip(docs, metas, distances):
                    p_id = meta.get("project_id", "Desconocido")
                    if p_id not in grouped_projects:
                        grouped_projects[p_id] = {"chunks": [], "min_distance": float('inf')}
                    if doc not in grouped_projects[p_id]["chunks"]:
                        grouped_projects[p_id]["chunks"].append(doc)
                    if dist < grouped_projects[p_id]["min_distance"]:
                        grouped_projects[p_id]["min_distance"] = dist
            
            sorted_projects = sorted(grouped_projects.items(), key=lambda x: x[1]["min_distance"])[:3]
            for p_id, p_data in sorted_projects:
                dist = p_data["min_distance"]
                similitud_pct = max(0, min(100, (1.0 - dist) * 100))
                if similitud_pct > max_similitud_pct:
                    max_similitud_pct = similitud_pct
                similar_projects.append({
                    "title": p_id.upper(),
                    "content": " ".join(p_data["chunks"][:3]),
                    "similarity_pct": similitud_pct
                })

        words_count = len(full_text.split())
        academic_alignment = 50
        areas_of_improvement = []
        
        if words_count > 1000:
            academic_alignment += 20
        else:
            areas_of_improvement.append("El documento es demasiado corto, se recomienda extender el marco teórico.")
            
        if "bibliografía" in full_text.lower() or "referencias" in full_text.lower():
            academic_alignment += 15
        else:
            areas_of_improvement.append("No se detectó sección de bibliografía explícita.")
            
        if "objetivo" in full_text.lower() or "metodología" in full_text.lower():
            academic_alignment += 15
        else:
            areas_of_improvement.append("Faltan secciones clave como Objetivos o Metodología.")

        collision_risk_level = "Bajo"
        if max_similitud_pct > 60:
            collision_risk_level = "Alto"
        elif max_similitud_pct > 30:
            collision_risk_level = "Medio"

        quick_analysis = {
            "status": "success",
            "academic_alignment": min(100, academic_alignment),
            "collision_risk_pct": round(max_similitud_pct, 1),
            "collision_risk_level": collision_risk_level,
            "areas_of_improvement": areas_of_improvement
        }

        # Guardar Draft
        draft_path = os.path.join(DRAFTS_DIR, f"{user_id}_draft.json")
        draft_data = {
            "chunks": chunks,
            "similar_projects": similar_projects,
            "quick_analysis": quick_analysis
        }
        with open(draft_path, "w", encoding="utf-8") as f:
            json.dump(draft_data, f, ensure_ascii=False)

        return quick_analysis

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/draft-proposal/{user_id}")
async def get_draft_proposal(user_id: str):
    draft_path = os.path.join(DRAFTS_DIR, f"{user_id}_draft.json")
    if os.path.exists(draft_path):
        try:
            with open(draft_path, "r", encoding="utf-8") as f:
                draft_data = json.load(f)
            return draft_data.get("quick_analysis", {})
        except:
            return {"status": "not_found"}
    return {"status": "not_found"}

@router.post("/analyze-draft-proposal")
async def analyze_draft_proposal(user_id: str = Form(...)):
    draft_path = os.path.join(DRAFTS_DIR, f"{user_id}_draft.json")
    if not os.path.exists(draft_path):
        raise HTTPException(status_code=404, detail="No se encontró borrador para este usuario.")
        
    try:
        with open(draft_path, "r", encoding="utf-8") as f:
            draft_data = json.load(f)
            
        chunks = draft_data.get("chunks", [])
        similar_projects = draft_data.get("similar_projects", [])
        proposal_text = " ".join(chunks)
        
        if not ollama_service.check_health():
             return {
                 "status": "warning",
                 "message": "Ollama no está respondiendo en localhost:11434.",
                 "similar_projects": [p["title"] for p in similar_projects]
             }

        llm_verdict = ollama_service.analyze_originality(
            proposal_text=proposal_text,
            similar_projects=similar_projects
        )

        # Eliminar borrador tras éxito
        try:
            os.remove(draft_path)
        except:
            pass

        return {
            "status": "success",
            "message": "Análisis completado con Phi-3 Mini",
            "similar_projects_found": len(similar_projects),
            "ollama_analysis": llm_verdict
        }

    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/analyze-proposal-phi3")'''

    if '@router.post("/pre-validate-proposal")' in content:
        content = pattern.sub(new_code, content)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated {filepath}")
    else:
        print(f"Pattern not found in {filepath}")

update_routes("/home/eduartrob/Documentos/project9no/back/integratorProjectClustering-back-corvus/app/api/routes.py")
update_routes("/home/eduartrob/Documentos/project9no/pruebas/corvus-backend-local/app/api/routes.py")
