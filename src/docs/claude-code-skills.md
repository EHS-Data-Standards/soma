# Claude Code Skills for SOMA

SOMA includes a set of [Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview) skills that automate the pipeline from publication PDF to validated Excel spreadsheet. This guide explains how to set up Claude Code and use each skill.

## What Is Claude Code?

Claude Code is an AI assistant that lives in your terminal (the text-based command window on your computer). It can read your files, help you write and edit code, plan tasks, and work alongside you on projects. Think of it as a very capable helper that sits inside your coding environment.

### Important Things to Keep in Mind

Before diving into setup and skills, it is worth understanding what Claude Code is and is not. The following guidance is adapted from [Sabrina Toro, PhD](https://orcid.org/0000-0002-4142-7153) and the [OBO Academy](https://oboacademy.github.io/obook/), based on workshops and bootcamp training for curators and non-developers.

- **Claude is not an oracle.** It is an extremely efficient tool, but you should never rely on it alone to tell you *how* to do something. You need to provide it with context and information so it can help you find the answer.
- **Claude is trained to please you.** It will tend to agree with you and show you what you want to see. This means it is not always the best partner for debating ideas or getting pushback. Be aware of this tendency.
- **Stay focused.** It is easy to go down a rabbit hole with Claude. Keep your task in mind and avoid scope creep.
- **You must be able to verify the work.** Claude cannot do work that you yourself cannot evaluate. If you ask it to extract data from a paper, you need to review the output against the source. If you ask it to suggest ontology terms, you need to confirm they are correct. Claude can suggest approaches you might not have thought of, but ultimately you decide what is right.

---

## Getting a Claude Account

Claude Code requires a paid plan. It is **not available on the free Anthropic tier**. The free tier gives you access to claude.ai for basic conversations, but Claude Code (and therefore these skills) require at least a Pro subscription or an API key.

### Option 1: Claude Pro Plan ($20/month)

1. Go to [claude.ai](https://claude.ai/) and create an account
2. Subscribe to the **Pro plan** ($20/month) under **Settings > Subscription**
3. Claude Code is included with Pro

This is the minimum required to use Claude Code and the SOMA skills. Pro gives you 5x the capacity of the free tier and access to all models.

### Option 2: Claude Max Plan ($100/month, recommended for heavy use)

1. Go to [claude.ai](https://claude.ai/) and create an account
2. Subscribe to the **Max plan** ($100/month) under **Settings > Subscription**
3. Claude Code is included with Max -- no API key needed

Max provides significantly higher rate limits (5x Pro), which is useful when running the full PDF-to-Excel pipeline repeatedly. A Max 20x tier is also available at $200/month.

### Option 3: Anthropic API (recommended for teams or automation)

1. Go to [console.anthropic.com](https://console.anthropic.com/) and create an Anthropic account
2. Add a payment method under **Settings > Billing**
3. Generate an API key under **Settings > API Keys**
4. Set the key in your environment: `export ANTHROPIC_API_KEY=sk-ant-...`

API billing is pay-per-use and suited for programmatic or team workflows.

### What if I only have a free account?

Claude Code is not available on the free plan. You will need to upgrade to at least the **Pro plan** ($20/month) to use Claude Code and the SOMA skills. You can sign up for free at [claude.ai](https://claude.ai/) and upgrade at any time from **Settings > Subscription**.

## Installing Claude Code

Install Claude Code globally via npm:

```bash
npm install -g @anthropic-ai/claude-code
```

Then launch Claude Code from the SOMA project root:

```bash
cd /path/to/soma
claude
```

If you are on the Max plan, Claude Code will open a browser window to authenticate on first launch. If you are using an API key, make sure `ANTHROPIC_API_KEY` is set in your shell environment before running `claude`.

The skills are defined in `.claude/skills/` and are automatically available when Claude Code runs inside the SOMA repository.

## The Skills

SOMA provides four skills that form a pipeline:

```
PDF --> /pdf-to-yaml --> /linkml-validate --> /yaml-to-excel
                              ^
                         /oaklib (ontology lookup)
```

### `/oaklib` - Ontology Term Lookup

Look up, search, and validate ontology terms (CURIEs) used in SOMA data files.

**Example usage:**

```
/oaklib
> Look up CHEBI:74481
> Search the Cell Ontology for "nasal epithelial cell"
> Validate that CL:0002603 is a real term
```

**Supported ontologies:** CHEBI, CL, UBERON, NCBITaxon, UO, OBI, GO, ECTO, PR, HP, PATO, CLO

**Output:** Term labels, definitions, ancestors, and cross-references printed directly in the chat.

---

### `/pdf-to-yaml` - Extract Data from a Publication

Reads a publication PDF and extracts structured assay/measurement data into a SOMA-compliant YAML file.

**Example usage:**

```
/pdf-to-yaml
> Extract data from docs/papers/smith2024-pm25-ciliary.pdf
```

**What it does:**

1. Reads the PDF (in 20-page chunks)
2. Identifies assay types, measurements, protocols, and exposure conditions
3. Maps entities to ontology terms (using `/oaklib` internally)
4. Generates a Container YAML file following SOMA naming conventions

**Output location:** `tests/data/valid/Container-<author><year>-<agent>-<focus>.yaml`

**Important constraints:**

- All numeric values must come from the paper (never hallucinated)
- Figure-derived values are marked as approximate
- Missing data is omitted, not guessed

---

### `/linkml-validate` - Validate YAML Against the Schema

Validates a SOMA YAML file against the LinkML schema to catch structural and type errors.

**Example usage:**

```
/linkml-validate
> Validate tests/data/valid/Container-liu2024-pm25-cftr.yaml
```

**What it does:**

1. Runs `linkml-validate` CLI for a quick syntax/structure check
2. Optionally runs the Python loader for deeper validation
3. Reports any errors (missing fields, invalid enums, type mismatches)

**Output:** Validation results printed in the chat. No files are created -- errors are reported for you to fix.

---

### `/yaml-to-excel` - Convert YAML to Excel

Converts a validated SOMA YAML file into a formatted Excel workbook.

**Example usage:**

```
/yaml-to-excel
> Convert tests/data/valid/Container-liu2024-pm25-cftr.yaml to Excel
```

**What it does:**

1. Loads and validates the YAML
2. Reads the LinkML scaffold (`project/excel/soma.xlsx`) for canonical tab names
3. Creates tabs for each non-empty collection (Metadata, Protocol, ExposureCondition, KeyEvent, assay tabs, output tabs, etc.)
4. Applies SOMA styling (blue headers, borders, auto-width columns)

**Output location:** `src/docs/<Author><Year>_<Agent>_<Focus>_SOMA.xlsx`

For example:

- `src/docs/Liu2024_PM25_CFTR_SOMA.xlsx`
- `src/docs/Montgomery2020_PM25_Mucociliary_SOMA.xlsx`

---

## Full Pipeline Example

Here is a typical workflow using all four skills in sequence:

```
> /pdf-to-yaml
  Extract data from docs/papers/liu2024-pm25-cftr.pdf

> /oaklib
  Verify that CHEBI:74481 is correct for PM2.5

> /linkml-validate
  Validate tests/data/valid/Container-liu2024-pm25-cftr.yaml

> /yaml-to-excel
  Convert tests/data/valid/Container-liu2024-pm25-cftr.yaml to Excel
```

The final Excel file will appear in `src/docs/` and can be downloaded from the [Artifacts](artifacts.md) page.

---

## Alternative: OpenCode (Open Source)

[OpenCode](https://github.com/opencode-ai/opencode) is an open source terminal-based AI coding agent that supports Anthropic Claude models (among many others). It can serve as an alternative to Claude Code if you prefer an open source tool or want to use your own API key without a Pro/Max subscription.

OpenCode does not support Claude Code skills (the `/oaklib`, `/pdf-to-yaml`, etc. commands above) directly, but you can use it as a general-purpose AI coding assistant within the SOMA repository using Claude models.

### Installing OpenCode

**macOS (Homebrew):**

```bash
brew install opencode-ai/tap/opencode
```

**Linux/macOS (install script):**

```bash
curl -fsSL https://raw.githubusercontent.com/opencode-ai/opencode/refs/heads/main/install | bash
```

**Go:**

```bash
go install github.com/opencode-ai/opencode@latest
```

### Connecting to Anthropic

You will need an Anthropic API key. Create one at [console.anthropic.com](https://console.anthropic.com/) under **Settings > API Keys** (requires a payment method for pay-per-use billing).

**Option A: Interactive setup**

Launch OpenCode and use the built-in connection wizard:

```bash
cd /path/to/soma
opencode
```

Inside the TUI, type `/connect` and select **Anthropic**. You can authenticate by entering your API key directly.

**Option B: Configuration file**

Create `~/.config/opencode/opencode.json` (global) or `opencode.json` in the SOMA project root (project-level):

```json
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "anthropic": {
      "options": {
        "apiKey": "{env:ANTHROPIC_API_KEY}"
      }
    }
  },
  "model": "anthropic/claude-sonnet-4-5",
  "small_model": "anthropic/claude-haiku-4-5"
}
```

Then set your API key in your shell profile (e.g., `~/.zshrc`):

```bash
export ANTHROPIC_API_KEY=sk-ant-...
```

### Enabling Extended Thinking

Claude models in OpenCode support extended thinking for deeper reasoning on complex tasks. Add a `models` block to your provider config:

```json
{
  "provider": {
    "anthropic": {
      "options": {
        "apiKey": "{env:ANTHROPIC_API_KEY}"
      },
      "models": {
        "claude-sonnet-4-5": {
          "options": {
            "thinking": {
              "type": "enabled",
              "budgetTokens": 16000
            }
          }
        }
      }
    }
  },
  "model": "anthropic/claude-sonnet-4-5"
}
```

### Running OpenCode in the SOMA Repo

```bash
cd /path/to/soma
opencode
```

Once in the TUI, you can ask it to run the same underlying commands that the Claude Code skills use:

```
> Run: uv run linkml-validate -s src/soma/schema/soma.yaml tests/data/valid/Container-liu2024-pm25-cftr.yaml
> Run: uv run runoak -i sqlite:obo:chebi info CHEBI:74481
> Run: uv run python scripts/yaml_to_excel.py --input tests/data/valid/Container-liu2024-pm25-cftr.yaml --output src/docs/output.xlsx
```

You can also run a single prompt non-interactively:

```bash
opencode -p "Validate all YAML files in tests/data/valid/ against the SOMA schema"
```

### Limitations vs Claude Code

- **No skills support**: OpenCode does not load `.claude/skills/` files. You need to provide instructions manually or use OpenCode's own [agent configuration](https://opencode.ai/docs/agents/) to replicate similar behavior.
- **Pay-per-use only**: There is no bundled subscription -- you pay Anthropic directly for API usage.
- **Different tool permissions model**: OpenCode has its own permission system for file writes, shell commands, etc.
