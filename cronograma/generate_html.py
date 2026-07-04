import json
from datetime import datetime, timedelta

# Read markdown data
with open('data.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

tasks = []

def parse_date(date_str):
    if date_str == 'None' or not date_str:
        return None
    try:
        # e.g., "Jun 18, 2026"
        d = datetime.strptime(date_str, "%b %d, %Y")
        return d
    except ValueError:
        return None

# Skip first two lines (header and separator)
for line in lines[2:]:
    parts = [p.strip() for p in line.split('|')]
    if len(parts) >= 7:
        task_id_str = parts[1]
        name = parts[2]
        start_date_str = parts[3]
        end_date_str = parts[4]
        status = parts[5]
        assignees = parts[6]

        start_date = parse_date(start_date_str)
        end_date = parse_date(end_date_str)

        if not end_date and not start_date:
            start_date = datetime(2026, 6, 1)
            end_date = datetime(2026, 6, 2)
        elif not start_date:
            start_date = end_date - timedelta(days=2)
        elif not end_date:
            end_date = start_date + timedelta(days=2)

        # Ensure end date is strictly after start date for Gantt
        if end_date <= start_date:
            end_date = start_date + timedelta(days=1)

        # Parse category to assign colors
        status_raw = status.lower()
        if ' - ' in status_raw:
            category, status_val = status_raw.split(' - ', 1)
        else:
            category = 'general'
            status_val = status_raw

        bar_class = 'bar-general'
        if category == 'bitacoras': bar_class = 'bar-bitacoras'
        if category == 'actividades': bar_class = 'bar-actividades'
        if category == 'codigo': bar_class = 'bar-codigo'
        if category == 'documentos': bar_class = 'bar-documentos'

        progress = 100 if status_val == 'terminado' else 0

        tasks.append({
            'id': f"Task_{task_id_str}",
            'name': name,
            'start': start_date.strftime("%Y-%m-%d"),
            'end': end_date.strftime("%Y-%m-%d"),
            'progress': progress,
            'custom_class': bar_class,
            'category': category,
            'status_val': status_val,
            'assignees': assignees if assignees != 'None' else 'Sin asignar'
        })

tasks_json = json.dumps(tasks, ensure_ascii=False)

html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ClickUp Clone - Gantt Gratis</title>
    <!-- Frappe Gantt CSS -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/frappe-gantt/0.6.1/frappe-gantt.css" />
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
    
    <style>
        :root {{
            --bg-dark: #1e1e1e;
            --surface: #2d2d2d;
            --text-main: #f1f1f1;
            --border: #3d3d3d;
            
            --bitacora: #9333ea;
            --actividad: #3b82f6;
            --codigo: #f59e0b;
            --documento: #10b981;
        }}

        body {{
            background-color: var(--bg-dark);
            color: var(--text-main);
            font-family: 'Inter', sans-serif;
            margin: 0;
            padding: 20px;
        }}

        header {{
            margin-bottom: 20px;
            display: flex;
            align-items: center;
            gap: 15px;
        }}

        h1 {{
            font-size: 1.8rem;
            margin: 0;
            font-weight: 600;
        }}

        .badge-free {{
            background: linear-gradient(135deg, #10b981, #059669);
            color: white;
            padding: 4px 10px;
            border-radius: 8px;
            font-size: 0.8rem;
            font-weight: 600;
        }}

        .gantt-container {{
            background: var(--surface);
            border-radius: 12px;
            border: 1px solid var(--border);
            overflow: hidden;
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
            padding: 20px;
            overflow-x: auto;
        }}

        /* Customizing Frappe Gantt for Dark Mode */
        .gantt .grid-header {{ fill: var(--surface); }}
        .gantt .grid-row {{ fill: var(--bg-dark); }}
        .gantt .grid-row:nth-child(even) {{ fill: var(--surface); }}
        .gantt .tick {{ stroke: var(--border); stroke-width: 1; }}
        .gantt .tick text {{ fill: #8b949e; font-family: 'Inter', sans-serif; font-size: 11px; }}
        
        .gantt .bar-label {{ fill: #fff; font-family: 'Inter', sans-serif; font-weight: 500; text-anchor: start; }}
        .gantt-container svg {{ background: var(--bg-dark); border-radius: 8px; }}

        /* Custom Bar Colors */
        .gantt .bar-bitacoras .bar {{ fill: var(--bitacora); }}
        .gantt .bar-bitacoras .bar-progress {{ fill: #7e22ce; }}
        
        .gantt .bar-actividades .bar {{ fill: var(--actividad); }}
        .gantt .bar-actividades .bar-progress {{ fill: #2563eb; }}
        
        .gantt .bar-codigo .bar {{ fill: var(--codigo); }}
        .gantt .bar-codigo .bar-progress {{ fill: #d97706; }}
        
        .gantt .bar-documentos .bar {{ fill: var(--documento); }}
        .gantt .bar-documentos .bar-progress {{ fill: #059669; }}

        .gantt .bar-wrapper:hover .bar {{ opacity: 0.8; stroke: white; stroke-width: 1; }}

        .view-controls {{
            margin-bottom: 20px;
        }}

        button {{
            background: var(--surface);
            border: 1px solid var(--border);
            color: var(--text-main);
            padding: 8px 16px;
            border-radius: 6px;
            cursor: pointer;
            transition: 0.2s;
            font-family: 'Inter', sans-serif;
            font-size: 0.9rem;
        }}

        button:hover {{
            background: #3d3d3d;
        }}

        button.active {{
            background: var(--actividad);
            border-color: var(--actividad);
        }}

        .legend {{
            display: flex;
            gap: 15px;
            margin-top: 15px;
            font-size: 0.85rem;
        }}

        .legend-item {{
            display: flex;
            align-items: center;
            gap: 6px;
        }}

        .dot {{ width: 12px; height: 12px; border-radius: 50%; }}
        .dot.bit {{ background: var(--bitacora); }}
        .dot.act {{ background: var(--actividad); }}
        .dot.cod {{ background: var(--codigo); }}
        .dot.doc {{ background: var(--documento); }}

    </style>
</head>
<body>

    <header>
        <h1>Cronograma del Proyecto</h1>
        <span class="badge-free">Gantt Gratis Desbloqueado</span>
    </header>

    <div class="view-controls">
        <button onclick="changeView('Quarter Day')" class="view-btn">Día (Zoom)</button>
        <button onclick="changeView('Half Day')" class="view-btn">Medio Día</button>
        <button onclick="changeView('Day')" class="view-btn">Día</button>
        <button onclick="changeView('Week')" class="view-btn active">Semana</button>
        <button onclick="changeView('Month')" class="view-btn">Mes</button>
    </div>

    <div class="gantt-container">
        <svg id="gantt"></svg>
    </div>

    <div class="legend">
        <div class="legend-item"><div class="dot bit"></div> Bitácoras</div>
        <div class="legend-item"><div class="dot act"></div> Actividades</div>
        <div class="legend-item"><div class="dot cod"></div> Código</div>
        <div class="legend-item"><div class="dot doc"></div> Documentos</div>
    </div>

    <!-- Frappe Gantt JS -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/frappe-gantt/0.6.1/frappe-gantt.min.js"></script>
    <script>
        var tasksData = {tasks_json};

        // Initialize Gantt
        var gantt = new Gantt("#gantt", tasksData, {{
            header_height: 50,
            column_width: 30,
            step: 24,
            view_modes: ['Quarter Day', 'Half Day', 'Day', 'Week', 'Month'],
            bar_height: 25,
            bar_corner_radius: 6,
            arrow_curve: 5,
            padding: 18,
            view_mode: 'Week',
            date_format: 'YYYY-MM-DD',
            custom_popup_html: function(task) {{
                // Custom tooltip on hover
                return `
                    <div style="background: #1e1e1e; padding: 12px; border-radius: 8px; border: 1px solid #3d3d3d; color: white; width: 220px;">
                        <h4 style="margin: 0 0 8px 0; font-size: 14px; color: #fff;">${{task.name}}</h4>
                        <p style="margin: 4px 0; font-size: 12px; color: #8b949e;"><b>Estado:</b> ${{task.status_val}}</p>
                        <p style="margin: 4px 0; font-size: 12px; color: #8b949e;"><b>Asignado:</b> ${{task.assignees}}</p>
                        <p style="margin: 4px 0; font-size: 12px; color: #8b949e;"><b>Progreso:</b> ${{task.progress}}%</p>
                    </div>
                `;
            }}
        }});

        // Change View Mode
        function changeView(mode) {{
            gantt.change_view_mode(mode);
            document.querySelectorAll('.view-btn').forEach(btn => btn.classList.remove('active'));
            event.target.classList.add('active');
        }}
        
        // Move the bar label outside the bar so it's always readable like ClickUp
        setTimeout(() => {{
            document.querySelectorAll('.gantt .bar-label').forEach(label => {{
                // Quick hack: adjust x position to place text outside
                let currentX = parseFloat(label.getAttribute('x'));
                label.setAttribute('x', currentX + 15);
            }});
        }}, 500);

    </script>
</body>
</html>
"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("HTML with Gantt Chart generated successfully!")
