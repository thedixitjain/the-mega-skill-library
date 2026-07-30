---
name: code-review
description: "Revisão completa de segurança e qualidade das mudanças não commitadas:"
category: engineering-core
source_repo: affaan-m/ECC
source_path: "docs/pt-BR/commands/code-review.md"
source_url: https://github.com/affaan-m/ECC/blob/HEAD/docs/pt-BR/commands/code-review.md
---
# Code Review

Revisão completa de segurança e qualidade das mudanças não commitadas:

1. Obtenha arquivos alterados: git diff --name-only HEAD

2. Para cada arquivo alterado, verifique:

**Problemas de Segurança (CRITICAL):**
- Credenciais, chaves de API ou tokens hardcoded
- Vulnerabilidades de SQL injection
- Vulnerabilidades de XSS
- Falta de validação de entrada
- Dependências inseguras
- Riscos de path traversal

**Qualidade de Código (HIGH):**
- Funções > 50 linhas
- Arquivos > 800 linhas
- Profundidade de aninhamento > 4 níveis
- Falta de tratamento de erro
- Statements de console.log
- Comentários TODO/FIXME
- Falta de JSDoc para APIs públicas

**Boas Práticas (MEDIUM):**
- Padrões de mutação (usar imutável no lugar)
- Uso de emoji em código/comentários
- Falta de testes para código novo
- Problemas de acessibilidade (a11y)

3. Gere relatório com:
   - Severidade: CRITICAL, HIGH, MEDIUM, LOW
   - Localização no arquivo e números de linha
   - Descrição do problema
   - Correção sugerida

4. Bloqueie commit se houver problemas CRITICAL ou HIGH

Nunca aprove código com vulnerabilidades de segurança!

---

**Source:** [`affaan-m/ECC`](https://github.com/affaan-m/ECC) → `docs/pt-BR/commands/code-review.md`
