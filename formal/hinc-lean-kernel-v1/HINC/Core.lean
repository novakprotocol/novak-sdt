import Mathlib

/-!
# HINC formal kernel

A small machine-checkable kernel for the common-crossing and hidden-infinitesimal-
noncommutativity calculations. It deliberately formalizes only the highest-value
algebraic core; it does not claim to formalize the full Gerstenhaber endomorphism
classification or the historical/publication claims.
-/

namespace HINC

variable {R : Type*} [CommRing R] [CharP R 2]

lemma two_eq_zero : (2 : R) = 0 := by
  norm_num

lemma neg_eq_self (a : R) : -a = a := by
  have h2 : (2 : R) = 0 := two_eq_zero
  calc
    -a = a - 2 * a := by ring
    _ = a := by rw [h2]; ring

lemma add_eq_zero_iff_eq (a b : R) : a + b = 0 ↔ a = b := by
  constructor
  · intro h
    calc
      a = a + b - b := by ring
      _ = -b := by rw [h]; ring
      _ = b := neg_eq_self b
  · intro h
    rw [h]
    have h2 : (2 : R) = 0 := two_eq_zero
    calc
      b + b = 2 * b := by ring
      _ = 0 := by rw [h2]; ring

/-- The reduced crossing `x (y - 1) = 0`. -/
structure CrossingPoint (R : Type*) [CommRing R] where
  x : R
  y : R
  rel : x * (y - 1) = 0

namespace CrossingPoint

variable (R)

def one : CrossingPoint R where
  x := 1
  y := 1
  rel := by ring

variable {R}

def mul (p q : CrossingPoint R) : CrossingPoint R where
  x := p.x * q.x
  y := p.y * q.y
  rel := by
    calc
      (p.x * q.x) * (p.y * q.y - 1) =
          (p.x * p.y) * (q.x * (q.y - 1)) +
            q.x * (p.x * (p.y - 1)) := by ring
      _ = 0 := by rw [q.rel, p.rel]; ring

theorem mul_assoc (p q r : CrossingPoint R) :
    mul (mul p q) r = mul p (mul q r) := by
  apply CrossingPoint.ext
  · simp [mul, _root_.mul_assoc]
  · simp [mul, _root_.mul_assoc]

theorem one_mul (p : CrossingPoint R) : mul (one R) p = p := by
  apply CrossingPoint.ext <;> simp [mul, one]

theorem mul_one (p : CrossingPoint R) : mul p (one R) = p := by
  apply CrossingPoint.ext <;> simp [mul, one]

theorem mul_comm (p q : CrossingPoint R) : mul p q = mul q p := by
  apply CrossingPoint.ext <;> simp [mul, _root_.mul_comm]

end CrossingPoint

/-- The even parity thickening of the crossing by a square-zero coordinate. -/
structure EvenPoint (R : Type*) [CommRing R] extends CrossingPoint R where
  e : R
  esq : e * e = 0

namespace EvenPoint

variable (R)

def one : EvenPoint R where
  x := 1
  y := 1
  rel := by ring
  e := 0
  esq := by ring

variable {R}

def mul (p q : EvenPoint R) : EvenPoint R where
  x := p.x * q.x
  y := p.y * q.y
  rel := by
    calc
      (p.x * q.x) * (p.y * q.y - 1) =
          (p.x * p.y) * (q.x * (q.y - 1)) +
            q.x * (p.x * (p.y - 1)) := by ring
      _ = 0 := by rw [q.rel, p.rel]; ring
  e := p.x * q.e + q.y * p.e
  esq := by
    have h2 : (2 : R) = 0 := two_eq_zero
    calc
      (p.x * q.e + q.y * p.e) * (p.x * q.e + q.y * p.e) =
          p.x^2 * (q.e * q.e) +
            2 * p.x * q.y * q.e * p.e +
            q.y^2 * (p.e * p.e) := by ring
      _ = 0 := by rw [q.esq, p.esq, h2]; ring

theorem mul_assoc (p q r : EvenPoint R) :
    mul (mul p q) r = mul p (mul q r) := by
  apply EvenPoint.ext
  · apply CrossingPoint.ext
    · simp [mul, _root_.mul_assoc]
    · simp [mul, _root_.mul_assoc]
  · simp [mul]
    ring

theorem one_mul (p : EvenPoint R) : mul (one R) p = p := by
  apply EvenPoint.ext
  · apply CrossingPoint.ext <;> simp [mul, one]
  · simp [mul, one]

theorem mul_one (p : EvenPoint R) : mul p (one R) = p := by
  apply EvenPoint.ext
  · apply CrossingPoint.ext <;> simp [mul, one]
  · simp [mul, one]

/-- Universal square-zero-coordinate defect between `p*q` and `q*p`. -/
def defect (p q : EvenPoint R) : R :=
  (p.x + p.y) * q.e + (q.x + q.y) * p.e

theorem defect_formula (p q : EvenPoint R) :
    (mul p q).e + (mul q p).e = defect p q := by
  simp [mul, defect]
  ring

theorem mul_comm_iff_defect_zero (p q : EvenPoint R) :
    mul p q = mul q p ↔ defect p q = 0 := by
  constructor
  · intro h
    have he : (mul p q).e = (mul q p).e := congrArg EvenPoint.e h
    have hz : (mul p q).e + (mul q p).e = 0 :=
      (add_eq_zero_iff_eq _ _).2 he
    rw [defect_formula] at hz
    exact hz
  · intro hz
    apply EvenPoint.ext
    · exact CrossingPoint.mul_comm p.toCrossingPoint q.toCrossingPoint
    · apply (add_eq_zero_iff_eq _ _).1
      rw [defect_formula]
      exact hz

/-- The two coefficient equations that kill the universal commutator defect. -/
def CenterEquations (p : EvenPoint R) : Prop :=
  p.e = 0 ∧ p.x + p.y = 0

theorem center_equations_commute (p : EvenPoint R)
    (hp : CenterEquations p) (q : EvenPoint R) :
    mul p q = mul q p := by
  rw [mul_comm_iff_defect_zero]
  rcases hp with ⟨he, hxy⟩
  simp [defect, he, hxy]

theorem center_equations_force_idempotent_x (p : EvenPoint R)
    (hp : CenterEquations p) : p.x * (p.x - 1) = 0 := by
  have hxy : p.x = p.y := (add_eq_zero_iff_eq p.x p.y).1 hp.2
  calc
    p.x * (p.x - 1) = p.x * (p.y - 1) := by rw [hxy]
    _ = 0 := p.rel

end EvenPoint

/-! ## Affine unit-group commutator kernel -/

/-- Affine multiplication `(a,c)(b,d) = (ab, ad+c)`. -/
def affineMul (p q : R × R) : R × R :=
  (p.1 * q.1, p.1 * q.2 + p.2)

/-- Inverse data for an affine pair, given a chosen scalar inverse. -/
def affineInvData (a ai c : R) : R × R :=
  (ai, -(ai * c))

/-- The scalar part of `p q p⁻¹ q⁻¹` with explicit inverse witnesses. -/
def affineCommFirst (a ai b bi : R) : R :=
  a * b * ai * bi

/-- The translation part of `p q p⁻¹ q⁻¹` with explicit inverse witnesses. -/
def affineCommSecond (a ai c b bi d : R) : R :=
  (a * b * ai) * (-(bi * d)) +
    (a * b) * (-(ai * c)) + a * d + c

theorem affine_commutator_first
    (a ai b bi : R) (hai : a * ai = 1) (hbi : b * bi = 1) :
    affineCommFirst a ai b bi = 1 := by
  calc
    affineCommFirst a ai b bi = (a * ai) * (b * bi) := by
      simp [affineCommFirst]
      ring
    _ = 1 := by rw [hai, hbi]; ring

theorem affine_commutator_second
    (a ai c b bi d : R) (hai : a * ai = 1) (hbi : b * bi = 1) :
    affineCommSecond a ai c b bi d =
      (a + 1) * d + (b + 1) * c := by
  have habai : a * b * ai = b := by
    calc
      a * b * ai = (a * ai) * b := by ring
      _ = b := by rw [hai]; ring
  have hab_aic : (a * b) * (ai * c) = b * c := by
    calc
      (a * b) * (ai * c) = (a * ai) * (b * c) := by ring
      _ = b * c := by rw [hai]; ring
  have hb_bid : b * (bi * d) = d := by
    calc
      b * (bi * d) = (b * bi) * d := by ring
      _ = d := by rw [hbi]; ring
  calc
    affineCommSecond a ai c b bi d =
        -(b * (bi * d)) - ((a * b) * (ai * c)) + a * d + c := by
      simp [affineCommSecond, habai]
      ring
    _ = -d - b * c + a * d + c := by rw [hb_bid, hab_aic]
    _ = (a + 1) * d + (b + 1) * c := by
      rw [neg_eq_self d, neg_eq_self (b * c)]
      ring

/-- Combined commutator formula for the affine unit law. -/
theorem affine_commutator_formula
    (a ai c b bi d : R) (hai : a * ai = 1) (hbi : b * bi = 1) :
    (affineCommFirst a ai b bi,
      affineCommSecond a ai c b bi d) =
      (1, (a + 1) * d + (b + 1) * c) := by
  apply Prod.ext
  · exact affine_commutator_first a ai b bi hai hbi
  · exact affine_commutator_second a ai c b bi d hai hbi

#print axioms CrossingPoint.mul_assoc
#print axioms EvenPoint.mul_assoc
#print axioms EvenPoint.defect_formula
#print axioms EvenPoint.mul_comm_iff_defect_zero
#print axioms EvenPoint.center_equations_commute
#print axioms EvenPoint.center_equations_force_idempotent_x
#print axioms affine_commutator_formula

end HINC
