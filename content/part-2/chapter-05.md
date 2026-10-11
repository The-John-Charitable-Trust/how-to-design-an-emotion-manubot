# Chapter 5: Rules vs. Prototypes

*Why the Great Debate Over Concepts Is a Faux Dichotomy*

*In the previous chapter, I argued that identity conditions belong upstream as conceptual constraints and that several influential theories relocate them downstream into categorization, prediction, learning, and cultural grouping. In this chapter, I show that a false dichotomy between classical and prototype theories encourages the same architectural inversion.*

*Contemporary concept theory typically frames the debate as a forced choice. Either concepts possess stable identity conditions, or they emerge through flexible patterns of categorization. Either we preserve conceptual structure, or we accommodate context, similarity, and typicality. Either classical theory prevails, or prototype theory does.*

*I reject this binary opposition because it rests on a false architectural premise.*

*Classical theorists correctly insist that concepts require identity conditions; without them, we cannot explain validity, error, disagreement, or reference. Prototype theorists correctly explain the role of similarity, typicality, contextual variation, and graded membership in human categorization. The error occurs when proponents collapse these distinct explanatory roles into a single account of concepts.*

*I therefore assign each theory its proper explanatory responsibility. Classical theory bears responsibility for specifying identity conditions. Prototype theory bears responsibility for explaining similarity, typicality, contextual variation, and graded categorization among admissible instances. Identity conditions determine what counts as an admissible instance; prototype effects explain variation among those instances. We do not have to choose between structure and variation because each belongs to a different level of the same conceptual architecture.*

*This distinction also motivates a computational refactoring of prototype theory. Rather than treating probabilistic structure as the basis of conceptual identity, I argue that a lexical concept possesses an upstream constraint structure that specifies its identity conditions. An object falls under a concept only if it satisfies those identity conditions. Once admitted, prototype effects explain the similarity, typicality, contextual relevance, and graded categorization of admissible instances rather than the identity of the concept itself. In effect, I recast prototype theory as a theory of categorization over conceptually admissible instances rather than as a theory of conceptual identity.*

*Deep learning and JavaScript both illustrate this architecture. Engineers specify computational architectures before training begins, and programmers define inheritance structures before creating objects. In neither case does downstream variation determine upstream structure. In Appendix E, I demonstrate this layered organization directly in Chrome DevTools.*

*I conclude that the longstanding opposition between classical and prototype theories results from assigning different explanatory responsibilities to the same level of analysis. Once identity conditions remain upstream and prototype effects operate downstream, the apparent conflict disappears.*

*In Chapter 6, I move from diagnosis to construction. Building on this architectural repair, I develop a goal-governed model of conceptual identity that explains how identity conditions constrain admissible variation without eliminating flexibility.*

[Notes](../references/notes/chapter-05.md) · [Bibliography](../references/bibliography/chapter-05.md)

In the previous chapter, I argued that identity conditions belong upstream as conceptual constraints and that several influential theories relocate them downstream into categorization, prediction, learning, and cultural grouping. In this chapter, I show that a false dichotomy between classical and prototype theories encourages the same architectural inversion.

Contemporary concept theory typically frames the debate as a forced choice. Either concepts possess stable identity conditions, or they emerge through flexible patterns of categorization. Either we preserve conceptual structure, or we accommodate context, similarity, and typicality. Either classical theory prevails, or prototype theory does.

I reject this binary opposition because it rests on a false architectural premise.

Classical theorists correctly insist that concepts require identity conditions; without them, we cannot explain validity, error, disagreement, or reference. Prototype theorists correctly explain the role of similarity, typicality, contextual variation, and graded membership in human categorization. The error occurs when proponents collapse these distinct explanatory roles into a single account of concepts.

I therefore assign each theory its proper explanatory responsibility. Classical theory bears responsibility for specifying identity conditions. Prototype theory bears responsibility for explaining similarity, typicality, contextual variation, and graded categorization among admissible instances. Identity conditions determine what counts as an admissible instance; prototype effects explain variation among those instances. We do not have to choose between structure and variation because each belongs to a different level of the same conceptual architecture.

This distinction also motivates a computational refactoring of prototype theory. Rather than treating probabilistic structure as the basis of conceptual identity, I argue that a lexical concept possesses an upstream constraint structure that specifies its identity conditions. An object falls under a concept only if it satisfies those identity conditions. Once admitted, prototype effects explain the similarity, typicality, contextual relevance, and graded categorization of admissible instances rather than the identity of the concept itself. In effect, I recast prototype theory as a theory of categorization over conceptually admissible instances rather than as a theory of conceptual identity.

Deep learning and JavaScript both illustrate this architecture. Engineers specify computational architectures before training begins, and programmers define inheritance structures before creating objects. In neither case does downstream variation determine upstream structure. In Appendix E, I demonstrate this layered organization directly in Chrome DevTools.

I conclude that the longstanding opposition between classical and prototype theories results from assigning different explanatory responsibilities to the same level of analysis. Once identity conditions remain upstream and prototype effects operate downstream, the apparent conflict disappears.

In Chapter 6, I move from diagnosis to construction. Building on this architectural repair, I develop a goal-governed model of conceptual identity that explains how identity conditions constrain admissible variation without eliminating flexibility.

CHAPTER VI

The Blueprint of Mind

The Theory of Constrained Identity

In the last chapter, I completed the diagnostic work. I argued that several influential strands of contemporary concept theory fail for an architectural reason rather than an empirical one: they push identity conditions downstream into categorization, prediction, learning, and cultural grouping.[@karl2010freeenergy],[@karl2010freeenergy] This reversal weakens our ability to explain sameness, error, and disagreement across contexts.[@karl2010freeenergy]

Before I can propose a coherent framework of concepts, I must first show why contemporary theorists mistakenly frame classical and prototype theories as mutually exclusive.[@object2017work, p. 126]

Many theorists frame the debate as a forced choice. They argue that concepts either possess rigid, rule-governed definitions or emerge through flexible, similarity-based categorization.[@anil2021definitions] They further argue that we must either preserve strict identity conditions or abandon them in order to accommodate flexibility. I reject that choice because it rests on a false architectural premise.

Classical theory characterizes concepts as rule-governed structures organized by necessary and sufficient conditions.[@object2017work, p. 126] In its naive essentialist form, it holds that every valid instance must share a fixed essence. On this view, a concept's identity conditions consist of the properties an instance must satisfy in order to count as an instance of that concept.

Prototype theories arose in response to the empirical weakness of strict classical definitions. Psychological work on categorization showed that people do not treat category membership as all-or-nothing, that some instances function as more typical than others, and that similarity plays a central role in classification.[@object2017work, p. 126],[@object2017work, p. 126] Prototype theorists therefore reconceived conceptual organization in terms of central tendencies, family resemblance, and graded similarity rather than fixed boundaries.

Both traditions identify a genuine explanatory problem, but their proponents assign that problem to the wrong level of analysis. Classical theorists seek identity conditions, yet in their naive essentialist formulations they often reduce those conditions to rigid classification rules.[@object2017work, p. 126] Prototype theorists explain categorization behavior, yet they often elevate similarity structure into the concept itself.[@object2017work, p. 126] In different ways, both infer what a concept is from how people categorize its instances, rather than treating identity conditions as the upstream constraints on categorization.

Classical theorists often reduce conceptual identity to rigid classification criteria.[@object2017work, p. 126] Prototype theorists often reduce it to patterns of similarity and typicality.[@object2017work, p. 126] In the first case, variation appears incompatible with conceptual identity. In the second, conceptual identity dissolves into patterns of resemblance. Neither approach adequately explains the architecture of concepts.

The binary opposition persists because classical and prototype theorists use the term concept to answer different questions. Classical theorists seek to explain identity conditions.

Prototype theorists seek to explain categorization.[@posner1968genesis] They create a false dichotomy only when they treat those questions as competing explanations rather than as distinct explanatory tasks.

If I adopt a purely classical view, I cannot explain why a robin and a penguin both qualify as birds while one consistently strikes people as a more typical example than the other without introducing additional explanatory mechanisms.[@object2017work, p. 126] If I adopt a purely prototype view, I cannot explain why a whale remains a mammal even when someone classifies it as a fish because of its appearance and behavior.[@object2017work, p. 126]

The faux dichotomy follows from collapsing the distinction between upstream constraint structures and downstream categorization behavior.[@barsalou1983adhoc] Once that distinction disappears, identity conditions and categorization appear to be mutually exclusive.

In a properly ordered architecture, classical and prototype theories do not function as rivals. They operate at different levels. Classical structure belongs at the level of the concept as a constraint class that fixes identity conditions. Prototype effects belong at the level of instance distributions and category formation over time.[@posner1968genesis]

Once I assign identity conditions and categorization to their proper explanatory levels, I can explain prototype phenomena without allowing them to determine conceptual identity. Typicality no longer competes with identity conditions. It presupposes them. Similarity-based categorization no longer replaces conceptual structure. I therefore treat similarity-based categorization as operating over admissible instantiations.[@object2017work, p. 126] Once I distinguish the explanatory roles of identity conditions and categorization, the apparent conflict becomes a division of labor.

This is why we cannot resolve the classical versus prototype binary by choosing a side. We must dissolve it by architectural clarification. In the next sections, I show how the same faux dichotomy appears in contemporary AI systems, particularly deep learning, and how object-oriented programming models such as JavaScript's prototype-based inheritance already resolve the problem in practice.[@object2017work, p. 126],[@object2017work, p. 126]

Contemporary AI, especially deep learning, gives us a concrete example.[@eric2023concepts] These systems learn from data, adapt to context, and produce graded, probabilistic outputs.[@eric2023concepts] Yet they function coherently only because constraint structures already shape what the system can receive, transform, optimize, and produce.[@eric2023concepts]

Many people interpret the behavior of deep learning systems as evidence that training data determines conceptual structure, but that interpretation is misleading. Before training begins, engineers specify an architecture consisting of representational roles, loss functions, admissible transformations, optimization procedures, and search spaces.[@eric2023concepts] During training, the model adjusts its parameters within those predefined constraints.

Even systems that optimize aspects of architecture, such as architecture search, meta-learning, dynamic computation graphs, and self-supervised pretraining, still search within higher-order constraints.[@eric2023concepts] They do not search without structure. The model may learn how to classify, generalize, and vary its outputs, but it does so inside a defined space of admissible operations.

This matters for concept theory because it exposes the same faux dichotomy in a technical domain. If we look only at the final output, we may see probability, variation, and similarity. If we look at the architecture, we see constraints, layers, functions, and admissible operations. The output looks prototype-like. The architecture supplies the constraint structure that makes such variation possible.

Deep learning therefore does not vindicate prototype theory as a theory of concepts. It vindicates prototype effects as a theory of instance distributions under fixed constraints.[@object2017work, p. 126] Classical structure and prototype behavior do not compete. They operate at different levels.

Prototype theorists reject the classical claim that concepts derive their identity from necessary and sufficient conditions. Instead, they argue that a lexical concept possesses a probabilistic rather than a definitional structure, such that an object falls under the concept when it satisfies a sufficient number of its characteristic properties.[@object2017work, p. 126] Similarity, typicality, contextual sensitivity, and graded membership then explain why some instances appear more representative than others.

I retain the empirical insights of prototype theory, but I reject the explanatory role that many proponents assign to them. Similarity, typicality, contextual sensitivity, and graded membership explain how people categorize admissible instances; they do not determine conceptual identity.

I therefore propose a computational refactoring of prototype theory. A lexical concept C possesses an upstream constraint structure that specifies its identity conditions. An object falls under C only if it satisfies those identity conditions. Once admitted, prototype effects explain the similarity, typicality, contextual relevance, and graded categorization of admissible instances rather than the identity of the concept itself.

We can see the same architecture in JavaScript. Unlike class-based languages, JavaScript uses prototype-based inheritance, whereby programmers define inheritance relationships before they instantiate individual objects.[@object2017work, p. 126] New objects inherit that structure while retaining the ability to override or extend inherited properties and methods. They do not acquire their identity by comparison with previously instantiated objects, nor do programmers derive the inheritance structure by clustering similar objects. Instead, programmers specify the inheritance structure first and instantiate objects within it.

The term prototype obscures this distinction because it refers to something fundamentally different from the psychological notion of a prototype. In JavaScript, a prototype specifies an inheritance relationship rather than a statistical exemplar, similarity centroid, or central tendency.[@posner1968genesis] The architectural lesson is therefore not that JavaScript implements prototype theory, but that it distinguishes upstream inheritance from downstream variation. I propose the same division of explanatory labor for concept theory. Classical theory bears responsibility for identity conditions. Prototype theory bears responsibility for explaining similarity, typicality, contextual variation, and graded categorization among admissible instances.[@posner1968genesis] Once those explanatory responsibilities are restored to their proper levels, the apparent conflict between the two theories disappears.

I illustrate this architecture in Appendix E, Chrome DevTools Demonstration of Layered Ontology. By expanding a JavaScript object's prototype chain in Chrome DevTools, we can inspect three distinct levels: concept-level constraint, instance-level realization, and the infrastructural layer that makes inheritance possible. The appendix matters because it turns the chapter's architecture into something observable.

Together, deep learning and JavaScript converge on the same lesson. Systems that preserve reuse, correction, error detection, and stable reference must fix identity conditions upstream and allow execution to vary downstream.[@object2017work, p. 126] Classical theorists mistake rigid classification rules for concepts. Prototype theorists mistake similarity structure for concepts. Both extract identity conditions from downstream categorization rather than treating those conditions as the upstream constraints that make categorization intelligible.[@anil2021definitions]

This provides an architectural clarification rather than a new metaphysics of concepts. By separating constraint from execution, I distinguish operational stability from ontological necessity.

The constraint layer fixes identity conditions for the purposes of reuse, correction, and reference within a system. It does not claim that those constraints are metaphysically necessary features of reality.[@eric2023concepts]

This architecture secures operational identity without returning to naive essentialism. It also permits flexibility without conceptual drift. With this obstruction removed, I can now articulate a coherent framework for concepts.

In this chapter, I have dissolved the classical-prototype opposition by assigning each theory its proper level. Classical theory preserves an indispensable truth: concepts require identity conditions, or they cannot support validity, error, disagreement, or reference. Prototype theory preserves a different truth: actual categorization involves typicality, similarity, learning, and graded behavior. The error lies in making either truth do the whole work. Classical theory turns identity into rigidity when it treats concepts as exceptionless rulebooks. Prototype theory turns flexibility into drift when it treats downstream similarity as the concept itself.[@posner1968genesis]

The deliverable of this chapter is the layered architecture that separates these functions. Identity conditions belong upstream at the level of constraint. Variation, typicality, learning, and context-sensitive recognition operate downstream over admissible instances. Deep learning supplies the technical example: flexible outputs depend on prior architectures of inputs, losses, transformations, optimization procedures, and admissible operations. The JavaScript prototype chain supplies the software example: it is not a vague average but an inspectable inheritance structure through which objects receive, override, and extend constraint-bearing form.[@object2017work, p. 126]

This architecture secures operational identity without restoring naive essentialism. It lets a concept constrain admissible instantiation without pretending that the constraint is a hidden substance in nature. It lets categories vary without asking variation to define the concept. It lets systems learn, classify, and adapt without allowing execution to replace identity conditions.[@object2017work, p. 126]

In this chapter, I have therefore answered the governing question directly: I do not have to choose between rigid classical essence and unconstrained prototype flexibility. I need a layered account in which structure and variation occupy different positions in the same architecture.

Chapter 6 now states that account positively as a goal-governed model of conceptual identity: a model in which identity conditions remain upstream while norm-governed grouping varies in execution.[@anil2021definitions]
