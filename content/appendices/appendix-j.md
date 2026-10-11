# Appendix J: Constructivist Computational Model of  Emotions

## A Hypothetical Architecture

I present this appendix as a formal, hypothetical specification of the Constructivist Computational Model of Emotions (CCME). The model specifies the functional roles and logical dependencies necessary to frame emotion as interpretive sign construction under biological constraint, rather than as a literal account of neural implementation.1

Before I examine the computational architecture, I want to stabilize several terms that appear throughout the model. These terms refer to distinct levels in the construction of emotion, and I do not treat them as interchangeable.2

A feeling is a metaperceived interoceptive state. It is the conscious registration of bodily  affective conditions such as arousal, tension, warmth, or unease. Feelings arise from biological  regulation and exist independently of any emotional interpretation.3

I define a referent in this model as a felt state that the system binds to a simulated situation under contextual constraint. At this stage, the system has linked bodily affect with a perceived or imagined circumstance, producing a structured affective situation.4

This usage departs from standard semiotic definitions, where the referent denotes an external object or state of affairs. I redefine the referent here to reflect the internal object of interpretation within the emotional system: not the world as such, but the world that the agent simulates and affectively registers.

An emotion construct emerges only when the agent commits to an emotion identifier under a governing goal. This act instantiates the corresponding emotion concept. Emotional meaning  therefore appears at the moment of interpretive commitment rather than during affective  activation or contextual simulation.5

The CCME also distinguishes emotion concepts from category schemas, which serve different architectural roles. A category schema is a learned predictive structure that organizes prior experience and supports comparison, ranking, and prediction during emotional simulation. An emotion concept, by contrast, is an identity-bearing type that encodes the conditions under which an agent may endorse an emotional interpretation.6  Schemas also participate in computational preparation, but plays a different role. They supply learned predictive structure for simulation, ranking, and manageable comparison. Computation can therefore retrieve and rank candidates using schema-guided expectations under concept-level constraints, but the agent still must select and identify the emotion under a governing goal. In short: schemas help the system predict and prioritize; concepts constrain admissibility and later become the object of commitment.7

I distinguish between computational processes and interpretive commitment. Computation, as I define it here, includes predictive simulation, allostatic regulation, retrieval of prior experience, prioritization under practical limits, and iterative schema revision under prediction error. These processes prepare, bias, and constrain the field of possible interpretations8. Within this architecture, they do not confer emotional meaning. They establish the conditions under which the agent can cross the meaning boundary.9

I use terms such as “application server,” “stored procedures,” and “queries” as structural metaphors to designate distinct functional roles within the architecture. These terms do not describe neural mechanisms. They clarify the division of labor between processes that simulate, regulate, retrieve, and update, and the act that interprets and commits. I use these metaphors to clarify a vital constraint in my model: computation can prepare and constrain possible interpretations, but it cannot generate meaning on its own. In this spirit, I offer the pseudocode to formalize dependencies and execution order without implying that the brain literally executes software instructions.10

Because I prioritize architectural coherence over mechanistic reduction, this model demands a clear division of labor. If emotion can go wrong, change under correction, and depend on concepts, the system must distinguish between processes that simulate or regulate and the act that interprets and commits.11 This appendix demonstrates one internally consistent way to formalize that distinction.

<img src="../../assets/figures/appendix-j/figure-aj-1.svg" />
<p align="center">**Figure AJ-1. CCME Architecture Overview**</p>

------------------------------------------------------------------------------------------------------------------------------------------------------
Figure AJ-1. Constructivist Computational Model of Emotions (CCME) -Conscious Emotional Cognition

I now introduce the architecture in visual and functional terms. Figures AJ-1 and AJ-2 present the CCME as a layered system where I define components by their operational roles rather than anchoring them to specific brain structures. The diagrams distinguish four major domains: stimulus activation, contextual framing, the Biological Intelligence Application Server, and agency. They also mark the meaning boundary between processes that prepare interpretation and the act through which the agent commits.12

Within the diagrams, I show the Database Lane as a visually distinct layer, but I do not treat it as an additional architectural domain. The database functions as the persistent memory substrate of the Biological Intelligence Application Server. It stores learned schemas, stored procedures, and conceptual repertoires that the system retrieves during computation. I separate it graphically only to illustrate retrieval and update operations during emotional processing.13

<img src="../../assets/figures/appendix-j/figure-aj-2.svg" />
<p align="center">**Figure AJ-2. CCME Database Lane Architecture**</p>

------------------------------------------------------------------------------------------------------------------------------------------------------
Figure AJ-2. Constructivist Computational Model of Emotions (CCME) -Non-Conscious Emotional Cognition

The flow begins with stimulus activation. An exteroceptive input reaches the agent within a determinate context. Context is no passive backdrop; it functions as a structural parameter. It shapes simulation, modulates relevance, and alters which category schemas the system retrieves from memory. Because a stimulus never occurs in isolation, this fully embedded situation provides the raw material for all subsequent processing.14

Next, the stimulus-context pair passes to what I designate as the Biological Intelligence Application Server. This metaphor captures a cluster of predictive and regulatory operations: simulating possible situations, managing the body budget allostatically, retrieving past experiences, and probabilistically weighting category schemas under prediction error. The server prepares and narrows the field by generating situation models, urgency gradients, and ranked conceptual candidates. It also revises schemas whenever persistent error demands refinement. Crucially, however, this computational stage represents neither the place nor the moment where interpretation actually occurs.15

From these operations, the system forms a structured referent: a felt state bound to a simulated situation under contextual constraint. This referent, together with ranked category schemas and prior emotion instances, then reaches agency. Here, ranking means the probabilistic ordering of stored experiences and schema matches that appear most relevant to the present referent. These ranked schemas retrieve associated emotion concepts, and those concepts form the candidate set that the system presents to the agent for interpretation. Only at this stage does interpretation occur. The agent evaluates candidate concepts against identity conditions and governing goals, assigns an identifier, and commits to an emotion construct. The diagrams visually encode this boundary, and the pseudocode that follows expresses it formally.16

The first substantive operations inside the Biological Intelligence Application Server involve simulation and interoceptive regulation. These processes establish the computational field within which interpretation later operates. They do not generate emotion. They generate structured constraint.17

Simulation begins when the architecture constructs a situation model. Given a stimulus within a context, the predictive machinery projects what occurs now and what likely occurs next. This projection maps predicted affordances, candidate threats, relevance gradients, and expected outcome trajectories under the current governing goal. For example, the stimulus “snake” on a dim trail activates a completely different simulated landscape than that same stimulus behind reinforced glass in a zoo. Context dynamically modulates the simulation space. Ultimately, this preparatory stage provides a scenario rather than a verdict: a structured set of possibilities against which the agent may later evaluate action and interpretation.18

Parallel to situation simulation, the system performs anticipatory regulation of the body budget. Allostatic prediction prepares energetic resources in light of environmental demand. This regulation generates arousal, urgency, cost expectations, and readiness states. These do not yet constitute emotional meaning. They represent dynamic adjustments that increase or decrease the agent’s capacity to respond. The organism does not wait for meaning before it prepares; preparation precedes interpretation.19

Felt awareness emerges from this regulatory activity. A heightened arousal state, elevated urgency, or constrained energy profile becomes phenomenally available. This availability carries causal significance. It biases attention and action tendency. Yet it remains semantically available.. It supplies raw intensity and valence, but it defers the final task of reference-marking to the interpretive stage.20

The crucial move occurs when the system binds feeling to the simulated situation. The system forms a referent that combines bodily readiness with a projected world-model under contextual constraint. This referent possesses structure but lacks interpretation. It serves as a candidate for meaning. Because the simulation remains probabilistic and the feeling remains real but not self-interpreting, error remains possible. A high-urgency state in a dim café may bind to a danger simulation, yet the simulation may prove mistaken. The architecture preserves this distinction deliberately. The bodily readiness state may persist even when the simulated situation misrepresents the world, because the feeling itself does not assert a proposition about the situation.21 Within this model, both affect and the felt state remain non-propositional; neither encodes a determinate evaluative judgment before interpretation.

Simulation and interoception establish the conditions under which the agent later constructs emotional meaning. They narrow the field of possibilities while shaping salience, urgency, and practical manageability. Yet, they do not confer meaning; he agent must still evaluate this referent against conceptual identity conditions and their governing goals.22

Once the preparatory machinery forms a structured referent, the Biological Intelligence Application Server accesses the database lane to retrieve and evaluate category schemas. At this stage, the agent does not yet ask, “Which emotion is this?” Instead, these background database queries address a more basic question: “Which category schemas can plausibly explain this referent under the present goal?”23

Category schemas are not mere collections of past episodes. They are concept-governed abstractions derived from prior experience. Each schema encodes predictive commitments: what features should co-occur, what costs the agent should expect, what actions tend to follow, and what outcomes historically satisfy or frustrate the governing goal. In this sense, each schema has an underlying concept with identity conditions that determine what counts as an instance. The system retrieves these schemas through what the model metaphorically calls stored procedures. The language of stored procedures does not imply literal SQL execution in the brain; it identifies a functional role. These stored procedures execute retrieval in a systematic, goal-sensitive manner, respecting the boundaries of prior learning.24

To initiate the search, stored procedures use conceptual constraints to run a targeted query in memory. The current referent, which occurs when the server integrates a raw feeling with a live situation model, activates a subset of category schemas whose predictive commitments match the present configuration. The active goal then filters this subset further. For example, under a harm-avoidance goal, the application server applies extra weight to threat schemas rather than novelty schemas. Under a social-belonging goal, interpersonal schemas dominate. Consequently, the database returns a broad candidate set rather than a single category.25

Each candidate schema then undergoes iterative evaluation. The schema generates predicted features and expected outcomes. The application server compares these predictions against the current referent and computes prediction error. Schemas that minimize error gain posterior weight; schemas that fail lose weight or trigger revision. Persistent error may lead to schema refinement, splitting, or the creation of a new category. Learning occurs at this level through structural adjustment of the schema network. The organism does not revise feeling; it revises the conceptual scaffolding that organizes feeling into interpretable patterns.26

Following this iterative cycle, the Biological Intelligence Application Server ranks schemas by posterior probability to keep comparisons manageable. This step narrows the interpretive field to the conceptual structures that best explain the present case. Only then does the server retrieve prior emotion instances that align with schemas holding the highest probability under the active goal. These instances represent historical meanings and the outcomes they produced. They function as evidential resources, not as binding templates. Consequently, the server presents a candidate hierarchy that reflects past experience, probabilistic fit, and goal relevance. This preparation does not yet confer emotional meaning; the agent must still decide whether the present referent satisfies a candidate concept’s identity conditions.27

After simulation, interoceptive regulation, category iteration, and instance retrieval complete their work, the agent reaches the interpretive stage. At this point, the application server has generated a structured referent, retrieved governing schemas, minimized prediction error, and ranked candidates under the governing goal, but no determinate emotional interpretation yet exists.28

At this stage, I need to clarify that the governing goal is never absent. Even when the agent does not consciously endorse an explicit project, there is a default hedonic-regulatory goal. The organism continuously works to maintain viability, reduce disruptive prediction error, preserve energy balance, and stabilize affective equilibrium. This background orientation supplies a minimal evaluative frame within which interpretation occurs. By default, the agent operates under a baseline hedonic-regulatory goal. However, when an explicit intentional aim arises, such as avoiding harm, securing belonging, or pursuing achievement, that new goal overrides the default state. Interpretation therefore never occurs in a vacuum. The agent always evaluates a referent relative to an active goal, whether it springs from the default hedonic drive or a specific intentional aim.29

The meaning boundary marks the transition from computation to commitment. It functions as a functional distinction within the model rather than a spatial boundary in the brain. On one side lie probabilistic weighting, predictive updating, and efficiency optimization. On the other side lies interpretation. The preparatory stages of the architecture perform necessary computational preparation by simulating contexts, retrieving schemas, and weighting candidate interpretations. Emotional meaning, however, does not arise within this computational layer; it emerges only when an agent commits to one interpretation as the governing emotional sign.30

Constructing this final sign requires a decisive interpretive act: the binding of a candidate emotion concept to the present referent under governing goals when the referent satisfies the concept’s identity conditions.31 This commitment answers to two strict constraints. First, the referent must satisfy the concept's structural requirements. Second, the concept must advance the active goal. The agent may reject a construction that undermines core purposes even if it meets the structural criteria. This judgment remains entirely normative rather than computational. The agent asks not only whether the concept fits, but whether it serves.32

When the agent commits to a concept, the application server assigns an identifier. This assignment marks the moment of commitment. The identifier binds the universal to this case and stabilizes the interpretation. What began as a field of weighted possibilities becomes a determinate emotion construct. The output therefore constitutes emotional meaning: an emotion sign instantiated through the binding of the concept to the present referent under the governing goal.33

Because commitment occurs at this boundary, error remains intelligible. The feeling may stay accurate and the simulation plausible while the committed concept fails relative to the outcome. If avoidance in response to a harmless stimulus undermines the agents purposes, the mismatch becomes an error signal. The next iteration revises schema weights or category structure. The feeling remains what it was while the sign system adjusts.34

I present the architecture as a C# code walkthrough. I use the code to clarify the functional structure of the computational model. The pseudocode demonstrates how the components I introduced above interact in sequence: stimulus activation, simulation, predictive processing, body-budget regulation, schema retrieval, candidate formation, and finally interpretive commitment. The code that follows therefore serves as a formal representation of the architecture I illustrated in the preceding diagrams.35

The scope of this demonstration is intentionally limited. It traces how a stimulus becomes an interpreted emotion construct under computational constraint. It does not address later revisions of meaning such as conscious reinterpretation or recognition updates.

The C# executables for the projects below are in the downloaded ZIP file under the matching project folders. Each folder includes a README with instructions for building, running, and reproducing the sample outputs.

<img src="../../assets/figures/appendix-j/figure-03.png" />
<p align="center">**Project 1 — Architecture Diagram**</p>

-----------------------------------------------------------------------------------------------------------------------------
Figure AJ-3. UML Class Diagram for PreparationTrace

<img src="../../assets/figures/appendix-j/figure-04.png" />
<p align="center">**Project 1 — Component Detail**</p>

------------------------------------------------------------------------------------------------------------------------------
Figure AJ-4. UML Object Diagram for PreparationTrace

Project 1 demonstrates the computational preparation layer of the model before any emotion exists. I make one proposition operationally explicit: simulation, prediction, bodily regulation, referent formation, and schema retrieval can all occur while emotional meaning remains absent. This matters because I argue that these processes prepare and constrain interpretation, but do not themselves confer meaning. The code therefore models an affective-cognitive trace rather than an emotion construct. It takes a stimulus, simulates a situation, registers bodily readiness, retrieves candidate schemas, and then stops before interpretive commitment. In that sense, the project remains deliberately incomplete. Its incompleteness carries the argument.

The rationale for the project is straightforward. A computational model of emotions must preserve a strict boundary between preparation and meaning. A model that outputs fear as soon as threat-related variables activate would collapse feeling, simulation, and prediction into emotion, which is precisely the confusion I strive to avoid. Project 1 therefore serves as a negative demonstration. It shows that even a rich preparatory state remains pre-emotional until an agent commits to an emotion concept under a governing goal.

The additional README test case, dotnet run -- dog, confirms the same point with an unfamiliar stimulus: the program changes the simulation, prediction, body budget, referent, and candidate schemas, but still refuses to construct an emotion before interpretation.

The run command is shown in the input image.

<img src="../../assets/figures/appendix-j/figure-05.png" />
<p align="center">**Project 1 — Run Command (Input)**</p>

The corresponding output is shown in the output image.

<img src="../../assets/figures/appendix-j/figure-06.png" />
<p align="center">**Project 1 — Output**</p>

At this stage, the system has fully prepared the field of possible interpretations, yet no emotional meaning exists. The next step introduces the operation that produces emotion: commitment to a concept under a governing goal.

<img src="../../assets/figures/appendix-j/figure-07.png" />
<p align="center">**Project 1 — Execution Result**</p>

----------------------------------------------------------------------------------------------------------------------------
Figure AJ-5: UML Object Diagram for Fear Instance

<img src="../../assets/figures/appendix-j/figure-08.png" />
<p align="center">**Project 1 — Final Output**</p>

----------------------------------------------------------------------------------------------------------------------------
Figure AJ-6: UML Object Diagram for Interest Instance

Project 2 demonstrates the interpretive layer of the model, where the agent constructs emotional meaning. It makes explicit the decisive operation that Project 1 deliberately withheld: commitment to a concept under a governing goal. Project 1 showed that simulation, prediction, bodily regulation, referent formation, and schema retrieval can all occur without producing emotion. Project 2 now shows that emotion emerges only when the agent selects a concept, binds it to the referent, and assigns an identifier under a goal.

Figures AJ-5 and AJ-6 show the decisive contrast. In Figure AJ-5, the agent operates under the goal safety, selects the concept fear, assigns the identifier Fear(snake), and orients action toward withdrawal. In Figure AJ-6, the stimulus remains a snake, but the governing goal changes to curiosity; the agent selects interest, assigns the identifier Interest(snake), and orients action toward cautious approach.

When the agent runs dotnet run -- snake safety, the program selects fear, assigns Fear(snake), and orients action toward withdrawal. When the agent runs dotnet run -- snake curiosity, the program selects interest, assigns Interest(snake), and orients action toward cautious approach. When the agent runs dotnet run -- dog safety, the program returns no qualifying concept, no identifier, and no action because the input does not satisfy the available interpretive conditions.

This project operationalizes the central claim of the model: computation does not produce meaning by itself; the agent achieves meaning through interpretive commitment. Emotional meaning does not reside in the stimulus, the body state, or predictive processing alone. It arises when the agent selects a concept, binds it to the referent, and commits to an identifier under a goal. Figures AJ-5 and AJ-6 show that the goal parameter crosses the meaning boundary: the agent does not merely process the snake; the agent constructs the snake as fear-relevant or interest-relevant.

The run command is shown in the following image.

<img src="../../assets/figures/appendix-j/figure-09.png" />
<p align="center">**Project 2 — Run Command (Input)**</p>

The corresponding output is shown in the following image.

<img src="../../assets/figures/appendix-j/figure-10.png" />
<p align="center">**Project 2 — Output**</p>

This execution completes the architecture. The system now produces an emotion, not because it simulates or predicts more accurately, but because the agent commits to a concept under constraint. If the goal changes, the meaning changes, even if all prior computational steps remain the same. The contrast between snake safety and snake curiosity demonstrates that emotional meaning remains goal-relative and capable of correction, while conceptual identity rather than computation governs the result.

I preserve sovereignty at the point of meaning within this architecture. Computation constrains and prepares. Interpretation governs. The server does not calculate emotional meaning. The agent achieves meaning through commitment under constraint.36

Having shown the completed interpretive output, I now move inside the executable trace to show how the program builds that result step by step. The next set of C# code blocks follow the CCME architecture in execution order. They begin with the interpreter’s governing goal, then proceed through stimulus registration, prediction, bodily regulation, referent formation, schema retrieval, concept selection, identifier assignment, and action orientation. This walkthrough matters because the model’s philosophical claim depends on the order of operations: computation may prepare meaning, but the agent’s interpretive commitment completes it.

//Interpreter Initialization

<img src="../../assets/figures/appendix-j/figure-11.png" />
<p align="center">**Code — Interpreter Initialization**</p>

This block initializes the execution environment and defines the interpreter’s governing inputs. The interpreter operates as a goal-governed agent that receives a stimulus and determines how much of the computational trace to expose through the verbose flag.

Within CCME, the interpreter corresponds to the CSS constituent: Interpreter (Goal). The interpreter does not passively receive meaning from computation. It governs evaluation by maintaining the agent’s current goal as a constraint on interpretation. The stimulus therefore enters the system already situated within an evaluative frame rather than in a neutral computational vacuum.

//CSS Constituent: Interpreter (Goal)

<img src="../../assets/figures/appendix-j/figure-12.png" />
<p align="center">**Code — CSS Constituent: Interpreter (Goal)**</p>

This block establishes the governing goal that constrains evaluation. The interpreter explicitly declares the goal before any simulation or prediction occurs.

Within CCME, the goal functions as an interpretive constraint, not as an outcome of computation. Computational processes can narrow possibilities, but they cannot determine meaning independently of the agent’s purposes. By fixing the goal at the beginning of execution, the program demonstrates that evaluation does not occur in a goal vacuum.

//Computational Stage: Simulation

<img src="../../assets/figures/appendix-j/figure-13.png" />
<p align="center">**Code — Computational Stage: Simulation**</p>

This block models the first computational stage of the architecture: simulation of the external situation.

The system constructs a predictive representation of the environment before emotional meaning emerges. Simulation generates a structured model of the situation in which the stimulus appears. At this stage, the program treats the snake as a potentially dangerous object in a low-visibility environment.

Simulation does not assign meaning. It produces the environmental model that later interpretive processes will evaluate.

//Computational Stage: Predictive Processing

<img src="../../assets/figures/appendix-j/figure-14.png" />
<p align="center">**Code — Computational Stage: Predictive Processing**</p>

This block represents the predictive processing layer.

The predictive system evaluates the simulated situation and generates expectations about possible outcomes. In this scenario, the model predicts danger and prepares a withdrawal response.

Prediction narrows the space of possible interpretations, but it does not yet commit to an emotion concept. The architecture therefore maintains a strict distinction between prediction and interpretation.

//Computational Stage: Body Budget Regulation

<img src="../../assets/figures/appendix-j/figure-15.png" />
<p align="center">**Code — Computational Stage: Body Budget Regulation**</p>

This block models allostatic regulation, often described in the model as body-budget management.

The system adjusts physiological readiness in response to predicted demands. Increased arousal prepares the organism for rapid action, creating a bodily state that the interpreter will later perceive.

The body budget generates affective readiness, not emotional meaning. It produces the energetic conditions under which interpretation becomes possible.

//CSS Constituent: Referent (Context)

<img src="../../assets/figures/appendix-j/figure-16.png" />
<p align="center">**Code — CSS Constituent: Referent (Context)**</p>

This block constructs the referent, which binds together the simulated situation and the metaperceived bodily state.

The referent corresponds to the CSS constituent Referent (Context). It integrates environmental representation with interoceptive awareness while remaining pre-interpretive. At this stage, the system has formed a structured situation for the interpreter, but the agent has not yet assigned an emotional category.

//Category Retrieval (Stored Procedures)

<img src="../../assets/figures/appendix-j/figure-17.png" />
<p align="center">**Code — Category Retrieval (Stored Procedures)**</p>

This block represents the retrieval of conceptual categories from memory.

In the computational metaphor used throughout the architecture, this retrieval process functions like stored procedures in a database. Each category contains learned patterns that the system uses to predict how the current referent might fit previously encountered situations.

Categories therefore supply candidate interpretations without determining which interpretation the agent ultimately commits to.

//CSS Constituent: Concept

<img src="../../assets/figures/appendix-j/figure-18.png" />
<p align="center">**Code — CSS Constituent: Concept**</p>

This block selects the emotion concept that best satisfies the structural constraints of the referent under the governing goal.

Emotion concepts function as universal-bearing types that define the identity conditions of possible emotional constructs. The concept of fear specifies what must be true for an emotional episode to count as fear.

The program therefore identifies the concept that fits the predicted threat conditions.

//CSS Constituent: Interpretation (Default Meaning)

<img src="../../assets/figures/appendix-j/figure-19.png" />
<p align="center">**Code — CSS Constituent: Interpretation (Default Meaning)**</p>

This block marks the transition from computation to interpretation.

The interpreter evaluates the referent relative to the governing goal and commits to a meaning. The act of interpretation transforms a field of weighted possibilities into a determinate judgment.

Within CCME, this moment constitutes the origin of emotional meaning.

//CSS Constituent: Identifier

<img src="../../assets/figures/appendix-j/figure-20.png" />
<p align="center">**Code — CSS Constituent: Identifier**</p>

This block assigns an identifier to the emotional instance.

The identifier stabilizes the interpretation by binding the selected concept to the specific referent. In this example, the system labels the emotional instance as Fear(snake).

The identifier therefore represents the moment of commitment within the architecture.

//CSS Constituent: Construct

<img src="../../assets/figures/appendix-j/figure-21.png" />
<p align="center">**Code — CSS Constituent: Construct**</p>

This block produces the final emotional construct.

The construct integrates the concept, the referent, and the interpretation into a coherent emotional episode that includes bodily manifestation and behavioral orientation.

At this point, the agent instantiates a complete emotional instance.

The formalization now stands complete. I present an architectural clarification of how emotion remains interpretive while operating under biological constraint. The model demonstrates that predictive simulation, allostatic regulation, category retrieval, and probabilistic updating narrow and structure the field of possibilities without generating emotional meaning. Computation prepares. It does not decide.37

By isolating the meaning boundary, the architecture preserves three features that any viable theory of emotion must explain: the possibility of error and correction, goal relativity, and conceptual identity. Because emotional meaning arises only at the point of commitment, error remains intelligible. A felt state may remain accurate as bodily registration while the interpretation bound to it fails relative to the outcome. Learning therefore occurs through the revision of schemas and category structures rather than the suppression of affect. The organism does not correct feeling. It corrects its sign system.38

The inclusion of stored procedures, category schemas, and prediction error updating shows that I can model learning and efficiency without collapsing interpretation into mechanism. Retrieval biases candidates. Simulation constrains affordances. Posterior weighting improves practical manageability. None of these operations possesses authority over meaning. Authority remains with the agent who evaluates identity conditions under a governing goal and assigns an identifier that stabilizes the construct.39

The CCME thus achieves a strict division of labor. Biological intelligence supplies readiness and probabilistic structure. Memory supplies conceptual resources shaped by past success and failure. Interpretation binds universals to particulars and commits to an evaluative orientation. Emotional meaning does not function as the output of a calculation. It constitutes the achievement of a judgment enacted within constraint.40

The CCME offers one coherent way to formalize that structure. If we understand emotion as interpretive rather than merely reactive, then we must preserve the distinction between constraint and commitment, between preparation and interpretation. The Constructivist Computational Model of Emotions (CCME) demonstrates such a distinction precisely without denying the predictive, regulatory, and learning capacities of the organism.

The agent does not calculate meaning; the agent achieves it.41
