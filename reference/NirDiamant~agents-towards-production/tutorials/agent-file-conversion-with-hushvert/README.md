<!-- Harvested from https://github.com/NirDiamant/agents-towards-production/blob/HEAD/tutorials/agent-file-conversion-with-hushvert/README.md -->
> **Source:** [`NirDiamant/agents-towards-production`](https://github.com/NirDiamant/agents-towards-production) → `tutorials/agent-file-conversion-with-hushvert/README.md`

![](https://europe-west1-atp-views-tracker.cloudfunctions.net/working-analytics?notebook=tutorials--agent-file-conversion-with-hushvert--readme)

# Giving Your Agent File-Conversion Abilities (Locally, Privately)

Agents receive files, not prompts: quarterly decks, contracts, spreadsheets, scans. Models read none of these natively, and the common fix (upload everything to a converter API) is a privacy regression and a metered bill for work the user's device could do for free. This tutorial builds the production answer: a two-lane conversion setup that converts locally whenever the device can, and meters only the office-document formats that genuinely need a server.

## Overview

Everything in this tutorial hangs off one routing rule: never pay, in money or in privacy, for a conversion a device can do itself.

- The **local lane** is [`@hushvert/engine`](https://europe-west1-atp-views-tracker.cloudfunctions.net/working-analytics?notebook=tutorials--agent-file-conversion-with-hushvert--readme&click=hushvert-engine-npm&target=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2F%40hushvert%2Fengine&text=%40hushvert%2Fengine), an MIT-licensed WebAssembly engine: images, HEIC, audio, archives, PDF page operations, and data files convert entirely in the browser. The bytes never touch a network, which you can verify in your own network tab.
- The **server lane** covers what browsers cannot do (office documents to PDF, PDF to Word, PDF/PPTX/XLSX to LLM-ready markdown, large video), exposed two ways: an MCP server your agent calls as a tool, and a plain REST API for pipelines.

## What You'll Learn

- **The two-lane routing rule** - which conversions never need to leave the device, and how to enforce the split so agents never spend credits on client-convertible formats.
- **Conversion as a tool call** - one config block that gives Claude Code, Cursor, or any MCP host a `convert_file` tool for the heavy formats.
- **The hosted API flow** - submit, upload, poll, download from Python, with idempotency keys and honest failure states.
- **Reading fidelity claims skeptically** - a benchmark that shows where converted markdown beats popular extractors (multi-column reading order) and where it does not (simple tables are a solved problem).

## Tutorial

### [Complete Tutorial: agent-file-conversion-tutorial.ipynb](./agent-file-conversion-tutorial.ipynb)

## Run in Google Colab

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NirDiamant/agents-towards-production/blob/main/tutorials/agent-file-conversion-with-hushvert/agent-file-conversion-tutorial.ipynb)

## Requirements

- Python 3.10+ for the notebook
- A hushvert API key for the server-lane sections: create a free account and a key at [hushvert.com/developers/keys](https://europe-west1-atp-views-tracker.cloudfunctions.net/working-analytics?notebook=tutorials--agent-file-conversion-with-hushvert--readme&click=hushvert-keys&target=https%3A%2F%2Fhushvert.com%2Fdevelopers%2Fkeys%3Futm_source%3Dagents-towards-production%26utm_medium%3Dgithub%26utm_campaign%3Dtutorial&text=hushvert%20developer%20keys) (one-time email code, no password; keys need a confirmed email). The free monthly allowance covers this whole tutorial without payment.
- Node.js 18+ only if you connect the MCP server to a local agent

## What You'll Build

A document-intake setup for production agents: local-lane conversions that cost nothing and leak nothing, a metered server lane for the heavy formats, and a benchmark-informed rule for choosing reconstruction over raw text extraction.
