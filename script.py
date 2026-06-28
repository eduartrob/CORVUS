import re

file_path = '/home/eduartrob/Documentos/project9no/front/landing-front-corvus/index.html'

with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()

replacements = {
    r'\bbg-dark-900\b': 'bg-light-surface dark:bg-dark-900',
    r'\bbg-dark-800\b': 'bg-light-surfaceHigh dark:bg-dark-800',
    r'\btext-white\b': 'text-light-onSurface dark:text-white',
    r'\btext-gray-400\b': 'text-light-onSurfaceVariant dark:text-gray-400',
    r'\btext-gray-300\b': 'text-light-onSurfaceVariant dark:text-gray-300',
    r'\bborder-dark-800\b': 'border-light-outlineVariant dark:border-dark-800',
    r'\bborder-white/5\b': 'border-light-outlineVariant dark:border-white/5',
    r'\bborder-white/10\b': 'border-light-outlineVariant dark:border-white/10',
    r'\bborder-white/20\b': 'border-light-outlineVariant dark:border-white/20',
}

for pattern, replacement in replacements.items():
    content = re.sub(pattern, replacement, content)

with open(file_path, 'w', encoding='utf-8') as file:
    file.write(content)

print("Replaced CSS classes successfully!")
