import marimo

__generated_with = "0.25.1"
app = marimo.App(
    width="medium",
    layout_file="layouts/attention-cognition-presentation.slides.json",
)


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.hstack([
        mo.image("images/misterrogers.png", height="75vh", style={"object-fit": "contain", "display": "block"}),
        mo.vstack([
            mo.md("# Won't you be my neighbor?"),
            mo.md("### A challenge, an opportunity and a very modest proposal")
        ], align="center")
    ], gap=5, align="center")
    return


@app.cell
def _(mo):
    mo.vstack([
        mo.image("images/hle.png", width="50%"),
        mo.vstack([
            mo.md("## A benchmark of expert-level academic questions to assess AI capabilities."),
            mo.md("### *Center for AI Safety, Scale AI & HLE Contributors* | *Consortium Nature volume 649, p. 1139-1146 (2026)*")
        ], gap=0, align="center")
    ], gap=5, align="center")
    return


@app.cell
def _(mo):
    mo.image("images/hle-themes.png")
    return


@app.cell
def _(mo):
    mo.iframe("https://lastexam.ai", height="900px")
    return


@app.cell
def _():
    return


@app.cell
def _(mo):
    mo.hstack([
        mo.vstack([
            mo.md("## In an anformation-rich world, the wealth of information means a dearth of something else: a scarcity of whatever it is that the information consumes. What information consumes is rather obvious: it consumes the **attention** of its recipients. Hence a wealth of information creates a **poverty of attention** and a need to allocate that attention efficiently among the overabundance of information sources that might consume it."),
            mo.md("### *Herbert Simon*")
        ], align="center"),
        mo.image("images/herbertsimon.jpeg", height="75vh", style={"object-fit": "contain", "display": "block"})
    ], gap=5, align="center")
    return


@app.cell
def _(mo):
    mo.hstack([
        mo.image("images/alberteinstein.png", height="70vh", style={"object-fit": "contain", "display": "block"}),
        mo.vstack([
            mo.md("## I have no special talent. I am only passionately curious."),
            mo.md("### *Albert Einstein*")
        ], align="center")
    ], gap=5, align="center")
    return


@app.cell
def _(mo):
    mo.hstack([
        mo.vstack([
            mo.md("## If you want to have good ideas you must have many ideas. Most of them will be wrong, and what you have to learn is which ones to throw away."),
            mo.md("### *Linus Pauling*")
        ], align="center"),
        mo.image("images/linuxpauling.png", height="75vh", style={"object-fit": "contain", "display": "block"})
    ], gap=5, align="center")
    return


@app.cell
def _(mo):
    image_container_left = mo.Html("""
        <div style="position: relative; display: inline-block;">
        <img src="https://via.placeholder.com/400x300" style="display: block; max-width: 100%; height: auto;">
        <div style="
            position: absolute;
            top: 50px;
            left: 50px;
            width: 100px;
            height: 60px;
            background-color: white;
            border: 1px solid #eee;
            box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
            border-radius: 4px;
        "></div>
    </div>
    """)
    return (image_container_left,)


@app.cell
def _(mo):
    text_content = mo.md("""
        ### Slide Title
        Your text goes here. Since this is in a `mo.md` element, you have full access to markdown features:
        - **Bold** and *italic* text
        - Bullett Points
        - [Links](https://marimo.io)
    """)
    return (text_content,)


@app.cell
def _(image_container_left, mo, text_content):
    mo.hstack([
        image_container_left,
        text_content
    ], align="center", justify="start")
    return


@app.cell
def _(mo):
    mo.vstack([
        mo.md("# Attention and Cognition"),
        mo.md("#### Geographic Learning and Thought")
    ], justify="center", align="center")
    return


@app.cell
def _(mo):
    mo.vstack([
        mo.md("# Attention"),
        mo.hstack([
            mo.vstack([
                mo.md("### What information consumes is rather obvious: it consumes the attention of its recipients. Hence a wealth of information creates a poverty of attention, and a need to allocate that attention efficiently among the overabundance of information sources that might consume it."),
                mo.md("### --Herbert Simon, 1971")
            ]),
            mo.image("images/herbertsimon.jpeg", width="350px")
        ], justify="space-around", align="center", gap=2)
    ], align="center")
    return


@app.cell
def _(mo):
    mo.vstack([
        mo.md("# Attention"),
        mo.hstack([
            mo.vstack([
                mo.md("### Attention is ‘a state in which cognitive resources are focused on certain aspects of the environment rather than on others and the central nervous system is in a state of readiness to respond to stimuli’."),
                mo.md("#### --American Psychological Association, 2020")
            ]),
            mo.md("""
                - Voluntary attention, arising from conscious participation
                - Involuntary attention that is captured by environmental stimuli
            """)
        ], justify="end", align="center", gap=2)
    ], align="center")
    return


@app.cell
def _():
    " ()."
    return


@app.cell
def _(mo):
    mo.vstack([
        mo.md("## Tupaia and Cook's Endeavour, 1769"),
        mo.image("images/tupaias-map.jpg", style={"object-fit": "contain"})
    ], align="center")
    return


@app.cell
def _():
    # Pierce's Pragmatics
    # 1. Firstness (the raw geometry or the basic data. This is what GIS does well.) Raw ingredients
    # 2. Secondness (concepts that require further description to other concepts. Not deep situational interpretation. An ontolgy--digital dictionaries. Universally understood data) Recipes
    # 3. Thirdness (a specific situation makes some things true at some times and places, and for a specific community.) Knowing if your guests are vegetarians or not. This could change the dinner.


    # GIS is like feeding chicken to vegetarians. It has no "thirdnedd"

    # Data, domain semantics, task, community
    # Data: raw ingredients
    # Domain Semantics: Ontologies, scientific knowledge
    # Task: the process, workflow and intention of why the data is being used
    # Community: Who. The standing, licensing, authoritativeness of those involved. 

    # Let machines infer the above model components from known variables and probabilities. Look at the latent variables. 
    return


if __name__ == "__main__":
    app.run()
