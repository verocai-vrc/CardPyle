# CardPyle

## 1) Sinopse curta
CardPyle é um **motor de jogo de cartas** em Python focado em **simplicidade, testabilidade e evolução incremental**. 
O projeto modela o domínio clássico (Deck/Mão/Campo/Cemitério), possui **loop de turno** enxuto (`DRAW → MAIN → END`) com **mana por turno**, e carrega **cartas/decks a partir de arquivos YAML**, mantendo a engine desacoplada de qualquer UI. Ideal para prototipar regras e iterar rapidamente.

---

## 2) Funcionalidades já implementadas
- **Modelo de domínio**:
  - `CardDef` (definição estática da carta) e `Card` (instância em jogo).
  - `CardType`, `Zone`/`ZoneType` (Deck, Hand, Field, Graveyard), `Player`, `Game`, `Phase`.
- **Zonas de jogo**:
  - Embaralhar (`shuffle`), comprar (`draw`), adicionar/remover cartas entre zonas.
- **Fluxo de partida/turno**:
  - Embaralha decks e **compra inicial de 5 cartas** por jogador.
  - Fases: `DRAW` (compra + preparo do turno) → `MAIN` (ações) → `END` (encerramento).
- **Sistema de mana por turno**:
  - `max_mana` cresce **+1 a cada turno** até o limite (padrão 10).
  - `available_mana` é **resetado** para `max_mana` no início do seu turno.
- **Jogar criaturas (validação de custo)**:
  - Verifica carta na mão, tipo `CREATURE`, **paga custo de mana** e respeita limite de campo (padrão 5).
- **Banco de cartas e decks externos**:
  - Cartas em `data/cards.yaml` (YAML).
  - Decks via `decks/*.yaml` **ou** listas Python em `decklists.py`.
- **Qualidade & testes**:
  - Testes `pytest` cobrindo fluxo básico (start, compra no turno, mana, jogar criatura, rotação de turno).
  - Lint com **Ruff** e checagem de tipos com **Mypy**.
  - Layout **src/** e API pública em `cardpyle/__init__.py`.

---

## 3) Próximos passos (to‑do)
- **Combate**:
  - Fase de combate; atacar criaturas/face; cálculo de dano; morte e envio automático ao cemitério.
  - Regras de “exaustão”/summoning sickness (opcional).
- **Regras & validações**:
  - Invariantes de zona; limites configuráveis; checagens de jogadas ilegais com erros claros.
  - Limpeza de dano/efeitos no fim do turno (se aplicável).
- **Economia de recursos**:
  - Balancear custos/mana; definir cap e curvas; eventuais recursos alternativos (se desejado).
- **Persistência e reprodutibilidade**:
  - Serialização do estado da partida (JSON) e **log de eventos** para replay/depuração.
- **Interface**:
  - CLI mínima para jogar turnos; depois UI (Pygame ou Web).
- **IA/Bot**:
  - Oponente básico para simulação e testes automatizados de balanceamento.
- **Deckbuilding**:
  - Validador de deck (tamanho, cópias máximas, tags) e presets.
- **Documentação**:
  - Exemplos de uso, guias para adicionar novas cartas/decks, políticas de contribuição.
