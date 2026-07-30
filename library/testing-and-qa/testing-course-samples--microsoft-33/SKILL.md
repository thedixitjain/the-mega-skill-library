---
name: testing-course-samples
description: "Preverite, ali se zvezki lekcij in vzorci kode izvajajo na živi Microsoft Foundry / Azure OpenAI postavitvi. Repo vsebuje zaganjalnik v scripts/validate-notebooks.ps1, ki brez glave izvrši vsak Python zvezek in izpiše matriko USPEŠNO/NEUSPEŠNO."
category: testing-and-qa
source_repo: microsoft/ai-agents-for-beginners
source_path: "translations/sl/.agents/skills/testing-course-samples/SKILL.md"
source_url: https://github.com/microsoft/ai-agents-for-beginners/blob/HEAD/translations/sl/.agents/skills/testing-course-samples/SKILL.md
---
# Testiranje vzorcev tečaja

Preverite, ali se zvezki lekcij in vzorci kode izvajajo na živi
Microsoft Foundry / Azure OpenAI postavitvi. Repo vsebuje zaganjalnik v
[`scripts/validate-notebooks.ps1`](../../../../../scripts/validate-notebooks.ps1), ki
brez glave izvrši vsak Python zvezek in izpiše matriko USPEŠNO/NEUSPEŠNO.

## Kdaj uporabiti
- "Preveri vse zvezke / vzorce proti moji naročnini Azure."
- "Hitro testiraj tečaj po nadgradnji paketov ali spremembi modelov."
- "Katere lekcije še vedno uspešno / neuspešno delujejo v živo?"

**Ne** uporabljajte tega za AI Smoke Test GitHub Action (ki preverja *razporejene*
gostujoče agente — glej [`tests/README.md`](../../../tests/README.md)). Ta spretnost
izvršuje zvezke lokalno.

## Pogoji (najprej preverite)
1. **Python 3.12+** s potrebnimi moduli tečaja: `python -m pip install -r requirements.txt`
   plus izvrševalnik: `python -m pip install nbconvert ipykernel`.
2. **`.env` v korenu repozitorija** (kopiraj iz [`.env.example`](../../../../../.env.example)) z vsaj:
   - `AZURE_AI_PROJECT_ENDPOINT` — končna točka projekta Foundry
     (`https://<account>.services.ai.azure.com/api/projects/<project>`)
   - `AZURE_AI_MODEL_DEPLOYMENT_NAME` — aktivna implementacija (npr. `gpt-5-mini`)
   - `AZURE_OPENAI_ENDPOINT` (`https://<account>.openai.azure.com`) in `AZURE_OPENAI_DEPLOYMENT`
     za lekcije, ki neposredno kličejo Azure OpenAI (Lekcija 06, 02-azure-openai, 14 predaja/človeški zanke).
3. **`az login`** je zaključen — vzorci se prijavijo z `AzureCliCredential` (Entra ID, brez ključa).
4. Preverite, da izvajanje modela obstaja:
   `az cognitiveservices account deployment list -g <rg> -n <account> -o table`.

## Izvajanje preverjanja
```powershell
# Vsi Python zvezki (preskoči .NET, .venv, site-packages, prevode, veščinske vire)
pwsh scripts/validate-notebooks.ps1

# Ena lekcija, z daljšim časovnim zamikom na posamezno celico
pwsh scripts/validate-notebooks.ps1 -Filter '08-*' -Timeout 600

# Samo našteti, kaj bi se izvedlo (brez izvedbe)
pwsh scripts/validate-notebooks.ps1 -List

# Izrecen interpreter (če `python` ni v PATH, npr. Windows Store alias)
pwsh scripts/validate-notebooks.ps1 -Python "C:/path/to/python.exe"
```
Skript zapiše izvršene kopije, dnevnike po zvezkih, in `results.json` v
`$env:TEMP\aiab-nbval` ter izstopi s številom napak.

Prehodne napake (HTTP 429 omejitve hitrosti z deljenim računom, občasna
težava z žetonom `AzureCliCredential` ali časovna prekoračitev) se samodejno ponovijo
(`-Retries`, privzeto 2, z zaostankom `-RetryDelaySeconds`, privzeto 20). Če se
izvaja model redno pojavlja napaka 429, preverite globalno TPM kvoto naročnine
(`az cognitiveservices usage list -l <region>`) — povišanje kapacitete ene same
implementacije ne pomaga, če je kvota *naročnine* izčrpana.

## Razlaga rezultatov
- `PASS` — zvezek se je uspešno izvedel od začetka do konca brez napak v celicah.
- `FAIL` — prikaže se prva vrstica z `*Error` / `*Exception`; odprite ustrezni
  `log_*.txt` datoteko v izhodni mapi za celoten sled napake.
- Napaka enega zvezka je omejena z `-Timeout` (na celico), zato se zataknjena
  celica s človek-v-zanki prikaže kot `StdinNotImplementedError` namesto da visi.

## Lekcije, ki zahtevajo dodatne vire (pričakovano ne uspejo brez njih)
| Lekcija | Dodatna zahteva |
|--------|-------------------|
| 05 Agentic RAG | Azure AI Search (`AZURE_SEARCH_SERVICE_ENDPOINT`, ključ) — ima vmesno pot v pomnilniku |
| 11 MCP / GitHub | GitHub MCP strežnik + PAT |
| 13 spomin (cognee) | `cognee` konfiguriran z ponudnikom modela |
| 15 uporaba brskalnika | Playwright brskalniki nameščeni (`playwright install`) + `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` |
| 17 lokalni agent | Foundry Local runtime + preneseni model Qwen (na napravi, brez oblaka) |
| `*-dotnet-*` zvezki | .NET Interactive jedro (privzeto izključeno; uporabi `-IncludeDotnet`) |

## Poročanje nazaj
Povzemite v tabeli USPEŠNO/NEUSPEŠNO združeni po lekcijah. Ločite prave regresije
(napake kode/konfiguracije za popravilo) od vrzeli v okolju (manjkajoči Search/Foundry Local/PAT),
in za vsak pravi spodrsljaj navedite neuspešno `log_*.txt` datoteko.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->

---

**Source:** [`microsoft/ai-agents-for-beginners`](https://github.com/microsoft/ai-agents-for-beginners) → `translations/sl/.agents/skills/testing-course-samples/SKILL.md`
