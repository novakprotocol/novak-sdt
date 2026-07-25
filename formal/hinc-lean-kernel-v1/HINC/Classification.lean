import HINC.Core

/-!
# Principal HINC endomorphism-classification kernel

This file formalizes the coefficient elimination and monoid laws for the two
principal graded strict Gerstenhaber endomorphism normal forms appearing in the
HINC manuscript.

It deliberately stops at the generator-coefficient level. The separate
manuscript argument that these generator equations extend to all cup products
and Gerstenhaber brackets is not yet formalized here.
-/

namespace HINC

variable {R : Type*} [CommRing R] [CharP R 2]

/-! ## Even image -/

/-- Coefficients of a general degree-one linear candidate
`r ↦ λr + βs`, `s ↦ ηr + δs`. -/
structure EvenRawCoeffs (R : Type*) where
  lam : R
  beta : R
  eta : R
  delta : R

namespace EvenRawCoeffs

/-- Generator equations obtained from `s² = 0` and `[r,s] = r`. -/
def GeneratorEquations (c : EvenRawCoeffs R) : Prop :=
  c.eta * c.eta = 0 ∧
    c.lam * c.delta + c.beta * c.eta = c.lam ∧
    c.beta = 0

/-- Normal form stated in the manuscript. -/
def NormalForm (c : EvenRawCoeffs R) : Prop :=
  c.beta = 0 ∧
    c.eta * c.eta = 0 ∧
    c.lam * (c.delta - 1) = 0

/-- The generator equations are equivalent to the complete even coefficient
normal form. -/
theorem generatorEquations_iff_normalForm (c : EvenRawCoeffs R) :
    GeneratorEquations c ↔ NormalForm c := by
  constructor
  · rintro ⟨heta, hbracket, hbeta⟩
    refine ⟨hbeta, heta, ?_⟩
    rw [hbeta] at hbracket
    have hld : c.lam * c.delta = c.lam := by
      simpa using hbracket
    calc
      c.lam * (c.delta - 1) = c.lam * c.delta - c.lam := by ring
      _ = 0 := by rw [hld]; ring
  · rintro ⟨hbeta, heta, hcross⟩
    refine ⟨heta, ?_, hbeta⟩
    have hld : c.lam * c.delta = c.lam := by
      calc
        c.lam * c.delta = c.lam * (c.delta - 1) + c.lam := by ring
        _ = c.lam := by rw [hcross]; ring
    rw [hbeta]
    simpa [hld]

end EvenRawCoeffs

/-- Normalized even endomorphism data. -/
structure EvenEndoData (R : Type*) [CommRing R] where
  lam : R
  delta : R
  eta : R
  eta_sq : eta * eta = 0
  crossing : lam * (delta - 1) = 0

namespace EvenEndoData

@[ext]
theorem ext {a b : EvenEndoData R}
    (hlam : a.lam = b.lam)
    (hdelta : a.delta = b.delta)
    (heta : a.eta = b.eta) : a = b := by
  cases a
  cases b
  simp_all

variable (R)

def one : EvenEndoData R where
  lam := 1
  delta := 1
  eta := 0
  eta_sq := by ring
  crossing := by ring

variable {R}

/-- Composition: the left argument is applied after the right argument. -/
def comp (a b : EvenEndoData R) : EvenEndoData R where
  lam := a.lam * b.lam
  delta := a.delta * b.delta
  eta := a.lam * b.eta + b.delta * a.eta
  eta_sq := by
    have h2 : (2 : R) = 0 := two_eq_zero
    calc
      (a.lam * b.eta + b.delta * a.eta) *
          (a.lam * b.eta + b.delta * a.eta) =
          a.lam^2 * (b.eta * b.eta) +
            2 * a.lam * b.delta * b.eta * a.eta +
            b.delta^2 * (a.eta * a.eta) := by ring
      _ = 0 := by rw [b.eta_sq, a.eta_sq, h2]; ring
  crossing := by
    calc
      (a.lam * b.lam) * (a.delta * b.delta - 1) =
          a.lam * a.delta * (b.lam * (b.delta - 1)) +
            b.lam * (a.lam * (a.delta - 1)) := by ring
      _ = 0 := by rw [b.crossing, a.crossing]; ring

theorem comp_assoc (a b c : EvenEndoData R) :
    comp (comp a b) c = comp a (comp b c) := by
  apply EvenEndoData.ext
  · simp [comp, _root_.mul_assoc]
  · simp [comp, _root_.mul_assoc]
  · simp [comp]
    ring

theorem one_comp (a : EvenEndoData R) : comp (one R) a = a := by
  apply EvenEndoData.ext <;> simp [comp, one]

theorem comp_one (a : EvenEndoData R) : comp a (one R) = a := by
  apply EvenEndoData.ext <;> simp [comp, one]

/-- Forget the proof fields and restore the eliminated `β = 0` coordinate. -/
def toRaw (a : EvenEndoData R) : EvenRawCoeffs R where
  lam := a.lam
  beta := 0
  eta := a.eta
  delta := a.delta

theorem toRaw_satisfies (a : EvenEndoData R) :
    EvenRawCoeffs.GeneratorEquations a.toRaw := by
  rw [EvenRawCoeffs.generatorEquations_iff_normalForm]
  exact ⟨rfl, a.eta_sq, a.crossing⟩

/-- Principal even classification theorem: the raw generator equations hold
exactly for a normalized triple `(λ,δ,η)` with `β = 0`. -/
theorem principal_classification (c : EvenRawCoeffs R) :
    EvenRawCoeffs.GeneratorEquations c ↔
      ∃ a : EvenEndoData R,
        a.lam = c.lam ∧ a.delta = c.delta ∧ a.eta = c.eta ∧ c.beta = 0 := by
  constructor
  · intro h
    have hn := (EvenRawCoeffs.generatorEquations_iff_normalForm c).1 h
    refine ⟨{
      lam := c.lam
      delta := c.delta
      eta := c.eta
      eta_sq := hn.2.1
      crossing := hn.2.2
    }, rfl, rfl, rfl, hn.1⟩
  · rintro ⟨a, hlam, hdelta, heta, hbeta⟩
    rw [EvenRawCoeffs.generatorEquations_iff_normalForm]
    refine ⟨hbeta, ?_, ?_⟩
    · simpa [heta] using a.eta_sq
    · simpa [hlam, hdelta] using a.crossing

end EvenEndoData

/-! ## Odd image -/

/-- Coefficients of the most general homogeneous generator candidate used in
the odd classification. -/
structure OddRawCoeffs (R : Type*) where
  x : R
  lam : R
  mu : R
  p : R
  q : R
  rho : R
  sigma : R

namespace OddRawCoeffs

/-- Direct generator equations from the displayed bracket relations and the
remaining algebra relation. -/
def GeneratorEquations (c : OddRawCoeffs R) : Prop :=
  c.x = 0 ∧
    c.mu * c.lam = c.lam ∧
    c.mu * c.rho = c.rho ∧
    c.sigma = 0 ∧
    c.lam * c.rho = c.p ∧
    c.q = 0 ∧
    c.mu * c.rho = c.lam * c.p^2

/-- Diagonal normal form stated in the manuscript. -/
def NormalForm (c : OddRawCoeffs R) : Prop :=
  c.x = 0 ∧
    c.q = 0 ∧
    c.sigma = 0 ∧
    c.p = c.lam * c.rho ∧
    c.rho = c.lam * c.p^2 ∧
    c.lam * (c.mu - 1) = 0 ∧
    c.rho * (c.mu - 1) = 0

/-- The direct odd generator equations are equivalent to the complete diagonal
normal form. -/
theorem generatorEquations_iff_normalForm (c : OddRawCoeffs R) :
    GeneratorEquations c ↔ NormalForm c := by
  constructor
  · rintro ⟨hx, hmulam, hmurho, hsigma, hlrhop, hq, hlast⟩
    refine ⟨hx, hq, hsigma, hlrhop.symm, ?_, ?_, ?_⟩
    · calc
        c.rho = c.mu * c.rho := hmurho.symm
        _ = c.lam * c.p^2 := hlast
    · calc
        c.lam * (c.mu - 1) = c.mu * c.lam - c.lam := by ring
        _ = 0 := by rw [hmulam]; ring
    · calc
        c.rho * (c.mu - 1) = c.mu * c.rho - c.rho := by ring
        _ = 0 := by rw [hmurho]; ring
  · rintro ⟨hx, hq, hsigma, hp, hrho, hlam, hrhor⟩
    have hmulam : c.mu * c.lam = c.lam := by
      calc
        c.mu * c.lam = c.lam * (c.mu - 1) + c.lam := by ring
        _ = c.lam := by rw [hlam]; ring
    have hmurho : c.mu * c.rho = c.rho := by
      calc
        c.mu * c.rho = c.rho * (c.mu - 1) + c.rho := by ring
        _ = c.rho := by rw [hrhor]; ring
    refine ⟨hx, hmulam, hmurho, hsigma, hp.symm, hq, ?_⟩
    calc
      c.mu * c.rho = c.rho := hmurho
      _ = c.lam * c.p^2 := hrho

end OddRawCoeffs

/-- Normalized odd endomorphism data. -/
structure OddEndoData (R : Type*) [CommRing R] where
  lam : R
  mu : R
  p : R
  rho : R
  p_eq : p = lam * rho
  rho_eq : rho = lam * p^2
  lam_crossing : lam * (mu - 1) = 0
  rho_crossing : rho * (mu - 1) = 0

namespace OddEndoData

@[ext]
theorem ext {a b : OddEndoData R}
    (hlam : a.lam = b.lam)
    (hmu : a.mu = b.mu)
    (hp : a.p = b.p)
    (hrho : a.rho = b.rho) : a = b := by
  cases a
  cases b
  cases hlam
  cases hmu
  cases hp
  cases hrho
  rfl

variable (R)

def one : OddEndoData R where
  lam := 1
  mu := 1
  p := 1
  rho := 1
  p_eq := by ring
  rho_eq := by ring
  lam_crossing := by ring
  rho_crossing := by ring

variable {R}

/-- Coordinatewise composition of diagonal odd endomorphisms. -/
def comp (a b : OddEndoData R) : OddEndoData R where
  lam := a.lam * b.lam
  mu := a.mu * b.mu
  p := a.p * b.p
  rho := a.rho * b.rho
  p_eq := by
    calc
      a.p * b.p = (a.lam * a.rho) * (b.lam * b.rho) := by
        rw [a.p_eq, b.p_eq]
      _ = (a.lam * b.lam) * (a.rho * b.rho) := by ring
  rho_eq := by
    calc
      a.rho * b.rho = (a.lam * a.p^2) * (b.lam * b.p^2) := by
        rw [a.rho_eq, b.rho_eq]
      _ = (a.lam * b.lam) * (a.p * b.p)^2 := by ring
  lam_crossing := by
    calc
      (a.lam * b.lam) * (a.mu * b.mu - 1) =
          a.lam * a.mu * (b.lam * (b.mu - 1)) +
            b.lam * (a.lam * (a.mu - 1)) := by ring
      _ = 0 := by rw [b.lam_crossing, a.lam_crossing]; ring
  rho_crossing := by
    calc
      (a.rho * b.rho) * (a.mu * b.mu - 1) =
          a.rho * a.mu * (b.rho * (b.mu - 1)) +
            b.rho * (a.rho * (a.mu - 1)) := by ring
      _ = 0 := by rw [b.rho_crossing, a.rho_crossing]; ring

theorem comp_assoc (a b c : OddEndoData R) :
    comp (comp a b) c = comp a (comp b c) := by
  apply OddEndoData.ext <;> simp [comp, _root_.mul_assoc]

theorem comp_comm (a b : OddEndoData R) : comp a b = comp b a := by
  apply OddEndoData.ext <;> simp [comp, _root_.mul_comm]

theorem one_comp (a : OddEndoData R) : comp (one R) a = a := by
  apply OddEndoData.ext <;> simp [comp, one]

theorem comp_one (a : OddEndoData R) : comp a (one R) = a := by
  apply OddEndoData.ext <;> simp [comp, one]

/-- Restore the eliminated off-diagonal coefficients. -/
def toRaw (a : OddEndoData R) : OddRawCoeffs R where
  x := 0
  lam := a.lam
  mu := a.mu
  p := a.p
  q := 0
  rho := a.rho
  sigma := 0

theorem toRaw_satisfies (a : OddEndoData R) :
    OddRawCoeffs.GeneratorEquations a.toRaw := by
  rw [OddRawCoeffs.generatorEquations_iff_normalForm]
  exact ⟨rfl, rfl, rfl, a.p_eq, a.rho_eq, a.lam_crossing, a.rho_crossing⟩

/-- Principal odd classification theorem: the direct generator equations hold
exactly for a normalized diagonal quadruple `(λ,μ,p,ρ)`. -/
theorem principal_classification (c : OddRawCoeffs R) :
    OddRawCoeffs.GeneratorEquations c ↔
      ∃ a : OddEndoData R,
        a.lam = c.lam ∧ a.mu = c.mu ∧ a.p = c.p ∧ a.rho = c.rho ∧
          c.x = 0 ∧ c.q = 0 ∧ c.sigma = 0 := by
  constructor
  · intro h
    have hn := (OddRawCoeffs.generatorEquations_iff_normalForm c).1 h
    refine ⟨{
      lam := c.lam
      mu := c.mu
      p := c.p
      rho := c.rho
      p_eq := hn.2.2.2.1
      rho_eq := hn.2.2.2.2.1
      lam_crossing := hn.2.2.2.2.2.1
      rho_crossing := hn.2.2.2.2.2.2
    }, rfl, rfl, rfl, rfl, hn.1, hn.2.1, hn.2.2.1⟩
  · rintro ⟨a, hlam, hmu, hp, hrho, hx, hq, hsigma⟩
    rw [OddRawCoeffs.generatorEquations_iff_normalForm]
    refine ⟨hx, hq, hsigma, ?_, ?_, ?_, ?_⟩
    · simpa [hlam, hp, hrho] using a.p_eq
    · simpa [hlam, hp, hrho] using a.rho_eq
    · simpa [hlam, hmu] using a.lam_crossing
    · simpa [hrho, hmu] using a.rho_crossing

end OddEndoData

#print axioms EvenRawCoeffs.generatorEquations_iff_normalForm
#print axioms EvenEndoData.comp_assoc
#print axioms EvenEndoData.principal_classification
#print axioms OddRawCoeffs.generatorEquations_iff_normalForm
#print axioms OddEndoData.comp_assoc
#print axioms OddEndoData.comp_comm
#print axioms OddEndoData.principal_classification

end HINC
