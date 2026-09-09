<!-- generated-by: Claude Opus 4.8 | last_updated: 2026-09-09 -->
## eDMFT / IndmflParser

**Summary:** 6 mapped, 3 unmapped quantities (66.67% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `hybridization_window` | Unmapped | — |
| `real_or_imaginary_axis` | Unmapped | — |
| `n_corr_atoms` | Mapped | `runschema.method.DMFT.n_impurities` |
| `i_atom_corr` | Mapped | `runschema.method.AtomParameters.label` |
| `l_atom_corr` | Mapped | `runschema.method.AtomParameters.orbitals` |
| `siginds_corr` | Mapped | `runschema.method.AtomParameters.n_orbitals`<br>`runschema.method.AtomParameters.orbitals`<br>`runschema.method.DMFT.n_correlated_orbitals` |
| `siginds_corr.indep_cix_blocks` | Unmapped | — |
| `siginds_corr.cix` | Mapped | `runschema.method.AtomParameters.n_orbitals`<br>`runschema.method.DMFT.n_correlated_orbitals` |
| `siginds_corr.orbitals` | Mapped | `runschema.method.AtomParameters.orbitals` |

## eDMFT / ParamsParser

**Summary:** 4 mapped, 0 unmapped quantities (100.00% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `general_parameters` | Mapped | `runschema.method.HubbardKanamoriModel.double_counting_correction`<br>`runschema.method.DMFT.impurity_solver` |
| `general_parameters.params` | Mapped | `runschema.method.HubbardKanamoriModel.double_counting_correction`<br>`runschema.method.DMFT.impurity_solver` |
| `impurity_parameters` | Mapped | `runschema.method.HubbardKanamoriModel.u`<br>`runschema.method.HubbardKanamoriModel.jh`<br>`runschema.method.HubbardKanamoriModel.j`<br>`runschema.method.HubbardKanamoriModel.up`<br>`runschema.method.DMFT.n_electrons`<br>`runschema.method.DMFT.inverse_temperature` |
| `impurity_parameters.params` | Mapped | `runschema.method.HubbardKanamoriModel.u`<br>`runschema.method.HubbardKanamoriModel.jh`<br>`runschema.method.HubbardKanamoriModel.j`<br>`runschema.method.HubbardKanamoriModel.up`<br>`runschema.method.DMFT.n_electrons`<br>`runschema.method.DMFT.inverse_temperature` |

## eDMFT / ImpurityGfOutParser

**Summary:** 1 mapped, 0 unmapped quantities (100.00% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `parameters` | Mapped | `runschema.calculation.GreensFunctions.chemical_potential` |

## eDMFT / MaxentParamsParser

**Summary:** 1 mapped, 1 unmapped quantities (50.00% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `parameters` | Mapped | `runschema.method.FrequencyMesh.n_points`<br>`runschema.method.FrequencyMesh.points` |
| `smearing` | Unmapped | — |

## eDMFT / MaxEntSigOutParser

**Summary:** 0 mapped, 1 unmapped quantities (0.00% coverage).

| File-parser quantity | Status | Archive mapper source |
| --- | --- | --- |
| `aux_sigma` | Unmapped | — |
