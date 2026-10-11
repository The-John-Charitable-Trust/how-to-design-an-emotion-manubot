# Appendix D: Formal Reconstruction of the Posner-Keele Paradigm

## Why Statistical Abstraction Does Not Constitute Identity Conditions

In the Posner and Keele paradigm, the stimuli have a geometrically simple and mathematically precise structure. Each pattern consists of a fixed number n of dots positioned within a bounded coordinate system, such as a 30 × 30 grid. Formally, each stimulus can be represented as a vector in ℝ²ⁿ:

x = (x₁, y₁, …, xₙ, yₙ)

The unseen prototype is a single configuration:

P ∈ ℝ²ⁿ

and each training exemplar arises through distortion:

Iᵢ = P + εᵢ

where εᵢ is a noise vector. The empirical finding is that participants later classify novel patterns in accordance with an inferred central tendency, even though they never saw P itself.<sup>1</sup> From this result, theorists often conclude that abstraction can occur without retrieving a stored canonical template.<sup>2</sup>

That conclusion is correct as far as it goes. Participants can approximate a central tendency, which in statistical terms corresponds to estimating:

P̂ = (1/k) Σᵢ₌₁ᵏ Iᵢ

Classification can then proceed by computing distance in the same space, for example by Euclidean metric:

d(x, P) = ‖x − P‖

and assigning category membership based on proximity.

The paradigm demonstrates the extraction of statistical regularities within a shared representational space.<sup>3</sup> By itself, however, it does not establish that those regularities constitute identity conditions. At most, it shows that agents can recover central tendencies under distortion. It does not show that central tendency can ground identity conditions for the concept.

The very computation of P̂ and d(x, P) presupposes that all instances inhabit the same fixed vector space ℝ²ⁿ. Dimensionality, coordinate structure, and admissible stimulus representation must stand prior to averaging or distance computation.<sup>4</sup> Within this already fixed space, the prototype functions as a statistical summary over admissible instances. It depends on the space for its definition and existence. It does not define that space.

Exemplar models, which compare a candidate x to stored instances Iᵢ rather than to P̂, operate in exactly the same space. Whether classification relies on the mean vector or on similarity to remembered exemplars, both procedures presuppose that valid stimuli are vectors in ℝ²ⁿ constrained by the same coordinate framework.

The dot-diagram paradigm secures identity conditions through this constraint structure. A legitimate instance must satisfy the structural specification:

x ∈ S ⊆ ℝ²ⁿ

where S encodes the fixed grid, fixed number of dots, and admissible coordinate bounds. Distortions modify coordinates, but they do not alter dimensionality or representational type. An instance may vary widely in position while remaining admissible because it satisfies the governing structural constraints of S.<sup>5</sup>

If theorists equate identity conditions with the statistical mean P̂, then any shift in distribution rewrites the concept. If they equate identity conditions with similarity regions defined by:

{x ∣ d(x, P̂) ≤ τ}

then a threshold, not a concept, carries the burden of definition. If they equate identity conditions with successful classification, convergence during learning functionally determines structure. The paradigm does not compel any of these conclusions. It shows only that agents can approximate central tendency under distortion within a fixed space.<sup>6</sup>

The deeper architectural claim is therefore this: statistical abstraction operates inside a constraint-defined representational space whose structure must exist independently of performance. The vector space ℝ²ⁿ, the bounded grid, and the admissibility constraints S make distortion, distance, averaging, and abstraction possible. Identity conditions reside at the level of that constraint specification. Identity belongs to an admissible instance under those conditions. Prototype estimation, exemplar comparison, and classification are execution-level operations within the space.

## Conclusion

I have therefore reconstructed the Posner-Keele result at the level where its real force can be seen. The experiment shows that agents can abstract a central tendency from distorted exemplars without first seeing the prototype. That result matters. It explains a form of learning, generalization, and statistical recovery. But it does not show that statistical abstraction supplies identity conditions.

The formal reconstruction exposes the prior structure the experiment requires. Averaging, distance, distortion, and classification all presuppose a fixed representational space: a determinate number of dots, a bounded coordinate system, and admissible locations within that system. The prototype estimate can summarize variation only because the space of possible instances has already been constrained. The threshold can sort candidates only because the relevant dimensions have already been fixed.

Appendix D therefore answers the governing question directly. Statistical central tendency is not conceptual identity. Similarity regions are not definitions. Successful classification is not the source of the concept it classifies. Identity conditions reside in the constraint specification that makes the statistical operation possible; identity belongs to an admissible instance under those conditions.

This appendix strengthens Chapter 4 by showing why partitioning cannot define what it partitions. The Posner-Keele paradigm supports abstraction within constraint, not abstraction in place of constraint. It therefore prepares the move into Chapter 5: the dispute between classical definitions and prototype theories cannot be resolved until I distinguish upstream admissibility conditions from downstream recognition, typicality, and similarity.

## Endnotes

1. Michael I. Posner and Steven W. Keele, "On the Genesis of Abstract Ideas," Journal of Experimental Psychology 77, no. 3 (1968): 353-363, https://doi.org/10.1037/h0025953. Access basis: DOI and author-uploaded full text.

2. Michael I. Posner and Steven W. Keele, "On the Genesis of Abstract Ideas," Journal of Experimental Psychology 77, no. 3 (1968): 353-363, https://doi.org/10.1037/h0025953. Access basis: DOI and author-uploaded full text.

3. Michael I. Posner and Steven W. Keele, "On the Genesis of Abstract Ideas," Journal of Experimental Psychology 77, no. 3 (1968): 353-363, https://doi.org/10.1037/h0025953. Access basis: DOI and author-uploaded full text.

4. Michael I. Posner and Steven W. Keele, "On the Genesis of Abstract Ideas," Journal of Experimental Psychology 77, no. 3 (1968): 353-363, https://doi.org/10.1037/h0025953. Access basis: DOI and author-uploaded full text.

5. Michael I. Posner and Steven W. Keele, "On the Genesis of Abstract Ideas," Journal of Experimental Psychology 77, no. 3 (1968): 353-363, https://doi.org/10.1037/h0025953. Access basis: DOI and author-uploaded full text.

6. Michael I. Posner and Steven W. Keele, "On the Genesis of Abstract Ideas," Journal of Experimental Psychology 77, no. 3 (1968): 353-363, https://doi.org/10.1037/h0025953. Access basis: DOI and author-uploaded full text.

## Bibliography

Posner, Michael I., and Stephen W. Keele. “*On the Genesis of Abstract Ideas*.” *Journal of Experimental Psychology* 77, no. 3 (1968): 353-63.
