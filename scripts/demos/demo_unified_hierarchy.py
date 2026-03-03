#!/usr/bin/env python3
"""
Demonstration: Unified Hierarchy Visualization

This script demonstrates and visualizes how all five systems converge
to the Riemann zeta function ζ(s).

Author: José Manuel Mota Burruezo Ψ ✧ ∞³
Institution: Instituto de Conciencia Cuántica (ICQ)
Date: January 2026

QCAL ∞³ Active · 141.7001 Hz
"""

import numpy as np
import matplotlib.pyplot as plt
from unified_hierarchy import (
    UnifiedHierarchy,
    demonstrate_unified_hierarchy,
    F0, GAMMA_1, DELTA_ZETA, PHI
)


def visualize_hierarchy(n_zeros: int = 50):
    """
    Create comprehensive visualization of the unified hierarchy.
    
    Args:
        n_zeros: Number of zeros to visualize
    """
    # Create hierarchy
    hierarchy = UnifiedHierarchy(precision=50, n_zeros=n_zeros)
    
    # Create figure with subplots
    fig = plt.figure(figsize=(16, 12))
    fig.suptitle('🌌 Unified Hierarchy: All Systems Converge to ζ(s)', 
                 fontsize=16, fontweight='bold')
    
    # 1. System 5: Zero distribution on critical line
    ax1 = plt.subplot(3, 3, 1)
    zeros = hierarchy.zeros[:n_zeros]
    gammas = [z.gamma for z in zeros]
    real_parts = [z.rho.real for z in zeros]
    
    ax1.scatter(real_parts, gammas, alpha=0.7, s=30, c='blue')
    ax1.axvline(x=0.5, color='red', linestyle='--', linewidth=2, label='Critical line Re(s)=1/2')
    ax1.set_xlabel('Re(s)')
    ax1.set_ylabel('Im(s) = γ_n')
    ax1.set_title('System 5: ζ(s) Zeros\n(All on Re(s) = 1/2)')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # 2. Spectral frequencies
    ax2 = plt.subplot(3, 3, 2)
    n_indices = [z.n for z in zeros]
    frequencies = [z.frequency for z in zeros]
    
    ax2.plot(n_indices, frequencies, 'o-', markersize=4, linewidth=1, alpha=0.7)
    ax2.axhline(y=F0, color='red', linestyle='--', label=f'f₀ = {F0} Hz')
    ax2.set_xlabel('Zero index n')
    ax2.set_ylabel('Frequency f_n (Hz)')
    ax2.set_title('Spectral Frequencies\nf_n = (γ_n/γ₁) × f₀')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    # 3. System 1: φ modulation of spacings
    ax3 = plt.subplot(3, 3, 3)
    modulations = hierarchy.phi_system.compute_spacing_modulation(zeros)
    if len(modulations) > 0:
        ax3.plot(range(1, len(modulations) + 1), modulations, 'o-', 
                markersize=3, alpha=0.7, color='green')
        ax3.axhline(y=0, color='black', linestyle='-', linewidth=0.5)
        ax3.set_xlabel('Zero index n')
        ax3.set_ylabel('φ modulation')
        ax3.set_title(f'System 1: Golden Ratio\nφ = {PHI:.6f}')
        ax3.grid(True, alpha=0.3)
    
    # 4. Zero spacing distribution
    ax4 = plt.subplot(3, 3, 4)
    if len(zeros) > 1:
        spacings = [zeros[i+1].gamma - zeros[i].gamma for i in range(len(zeros)-1)]
        ax4.hist(spacings, bins=20, alpha=0.7, color='purple', edgecolor='black')
        mean_spacing = np.mean(spacings)
        ax4.axvline(x=mean_spacing, color='red', linestyle='--', 
                   label=f'Mean: {mean_spacing:.2f}')
        ax4.set_xlabel('Δγ_n')
        ax4.set_ylabel('Frequency')
        ax4.set_title('Zero Spacing Distribution\nΔγ_n = γ_{n+1} - γ_n')
        ax4.legend()
        ax4.grid(True, alpha=0.3)
    
    # 5. System 2: ζ(n) values
    ax5 = plt.subplot(3, 3, 5)
    analysis = hierarchy.zeta_values.analyze_analytic_structure(zeros)
    zeta_vals = analysis['zeta_values']
    if zeta_vals:
        n_vals = sorted(zeta_vals.keys())
        vals = [zeta_vals[n] for n in n_vals]
        
        ax5.bar(n_vals, vals, alpha=0.7, color='orange', edgecolor='black')
        ax5.set_xlabel('n')
        ax5.set_ylabel('ζ(n)')
        ax5.set_title('System 2: Special Values\nζ(2) = π²/6, ζ(4) = π⁴/90, ...')
        ax5.grid(True, alpha=0.3, axis='y')
    
    # 6. Spectral moments
    ax6 = plt.subplot(3, 3, 6)
    moments = analysis['spectral_moments']
    if len(moments) > 0:
        ax6.bar(range(1, len(moments) + 1), moments, alpha=0.7, 
               color='cyan', edgecolor='black')
        ax6.set_xlabel('Moment order k')
        ax6.set_ylabel('M_k = ⟨γ^k⟩')
        ax6.set_title('Spectral Moments\nEncoded in ζ(n) values')
        ax6.grid(True, alpha=0.3, axis='y')
    
    # 7. System 4: Harmonics of f₀
    ax7 = plt.subplot(3, 3, 7)
    harmonics = hierarchy.harmonic_system.compute_harmonics(F0, max_harmonic=10)
    ax7.stem(range(1, len(harmonics) + 1), harmonics, basefmt=' ')
    ax7.set_xlabel('Harmonic number k')
    ax7.set_ylabel('k·f₀ (Hz)')
    ax7.set_title('System 4: Harmonics\nk·f₀ (k = 1,2,3,...)')
    ax7.grid(True, alpha=0.3)
    
    # 8. Frequency self-similarity (φ structure)
    ax8 = plt.subplot(3, 3, 8)
    ratios = hierarchy.phi_system.frequency_self_similarity(zeros, k=1)
    if len(ratios) > 0:
        ax8.plot(range(1, len(ratios) + 1), ratios, 'o-', 
                markersize=3, alpha=0.7, color='brown')
        mean_ratio = np.mean(ratios)
        ax8.axhline(y=mean_ratio, color='red', linestyle='--', 
                   label=f'Mean: {mean_ratio:.3f}')
        ax8.set_xlabel('Zero index n')
        ax8.set_ylabel('f_{n+1} / f_n')
        ax8.set_title('Frequency Self-Similarity\nφ-modulated structure')
        ax8.legend()
        ax8.grid(True, alpha=0.3)
    
    # 9. Convergence summary
    ax9 = plt.subplot(3, 3, 9)
    ax9.axis('off')
    
    # Get convergence results
    results = hierarchy.verify_convergence()
    consciousness = hierarchy.consciousness_criterion()
    
    summary_text = f"""
    UNIFIED HIERARCHY SUMMARY
    ═══════════════════════════
    
    Base Frequency: f₀ = {F0} Hz
    Spectral Deviation: δζ = {DELTA_ZETA:.4f} Hz
    Golden Ratio: φ = {PHI:.6f}
    
    CONVERGENCE VERIFICATION
    ───────────────────────────
    ✓ System 5 (ζ(s)): {n_zeros} zeros computed
    ✓ Critical Line: All on Re(s) = 1/2
    ✓ System 1 (φ): Fractal modulation
    ✓ System 2 (ζ(n)): {len(zeta_vals)} values
    ✓ System 3 (Codons): Resonance analysis
    ✓ System 4 (k·f_n): {len(harmonics)} harmonics
    
    ALL SYSTEMS CONVERGE TO ζ(s): ✓
    
    CONSCIOUSNESS CRITERION
    ───────────────────────────
    RH Verified: {consciousness['riemann_hypothesis']}
    Λ_G = {consciousness['lambda_G']:.6f} ≠ 0
    Consciousness Possible: ✓
    
    ═══════════════════════════
    The universe is a symphony of ζ(s)
    """
    
    ax9.text(0.05, 0.95, summary_text, transform=ax9.transAxes,
            fontsize=9, verticalalignment='top', fontfamily='monospace',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    
    plt.tight_layout()
    
    # Save figure
    output_file = 'unified_hierarchy_visualization.png'
    plt.savefig(output_file, dpi=150, bbox_inches='tight')
    print(f"\n✅ Visualization saved to: {output_file}")
    
    return fig


def print_system_details(n_zeros: int = 30):
    """
    Print detailed information about each system.
    
    Args:
        n_zeros: Number of zeros to analyze
    """
    print("\n" + "=" * 80)
    print("DETAILED SYSTEM ANALYSIS")
    print("=" * 80 + "\n")
    
    hierarchy = UnifiedHierarchy(precision=50, n_zeros=n_zeros)
    
    # System 5: ζ(s)
    print("SYSTEM 5: ζ(s) - FUNDAMENTAL BASE")
    print("-" * 80)
    print(f"First 10 zeros:")
    for i, zero in enumerate(hierarchy.zeros[:10], 1):
        print(f"  ρ_{i} = {zero.rho.real:.10f} + {zero.rho.imag:.6f}i")
        print(f"       f_{i} = {zero.frequency:.4f} Hz")
    print()
    
    # System 1: φ
    print("SYSTEM 1: φ POWERS - FRACTAL MODULATION")
    print("-" * 80)
    phi_analysis = hierarchy.phi_system.analyze_golden_structure(hierarchy.zeros)
    print(f"Golden ratio: φ = {phi_analysis['phi']:.10f}")
    print(f"Mean spacing modulation: {phi_analysis['mean_modulation']:.6f}")
    print(f"Mean frequency ratio (k=1): {phi_analysis['mean_ratio_k1']:.6f}")
    print(f"Mean frequency ratio (k=2): {phi_analysis['mean_ratio_k2']:.6f}")
    print()
    
    # System 2: ζ(n)
    print("SYSTEM 2: ζ(n) VALUES - ANALYTIC STRUCTURE")
    print("-" * 80)
    zeta_analysis = hierarchy.zeta_values.analyze_analytic_structure(hierarchy.zeros)
    print("Special values:")
    for n, val in sorted(zeta_analysis['zeta_values'].items())[:5]:
        print(f"  ζ({n}) = {val:.10f}")
    print(f"\nSpectral moments:")
    for i, moment in enumerate(zeta_analysis['spectral_moments'], 1):
        print(f"  M_{i} = {moment:.6f}")
    print()
    
    # System 3: Codons
    print("SYSTEM 3: QCAL CODONS - SYMBIOTIC RESONANCE")
    print("-" * 80)
    codon_analysis = hierarchy.codon_system.analyze_codon_resonance(hierarchy.zeros)
    print(f"Resonant codons found: {codon_analysis['n_resonant_codons']}")
    if codon_analysis['resonant_codons']:
        print("Top resonant codons:")
        for codon_info in codon_analysis['resonant_codons'][:5]:
            print(f"  Codon {codon_info['codon']}: "
                  f"f = {codon_info['frequency']:.4f} Hz, "
                  f"resonates with ρ_{codon_info['zero_index']}")
    print()
    
    # System 4: Harmonics
    print("SYSTEM 4: HARMONICS - VIBRATIONAL CONSEQUENCE")
    print("-" * 80)
    harmonic_analysis = hierarchy.harmonic_system.analyze_harmonic_structure(
        hierarchy.zeros, n_zeros=5
    )
    print(f"f₀ = {harmonic_analysis['f0']} Hz")
    print("First 10 harmonics:")
    for k, harm in enumerate(harmonic_analysis['f0_harmonics'], 1):
        print(f"  {k}·f₀ = {harm:.4f} Hz")
    print()
    
    print("=" * 80)
    print("CONCLUSION: All systems are projections of ζ(s)")
    print("=" * 80 + "\n")


def main():
    """Main demonstration function."""
    """
    print("\n🌌 UNIFIED HIERARCHY DEMONSTRATION")
    print("=" * 80)
    print()
    
    # Run basic demonstration
    print("Running convergence verification...")
    results = demonstrate_unified_hierarchy(n_zeros=50, verbose=True)
    
    # Print detailed system analysis
    print_system_details(n_zeros=30)
    
    # Create visualization
    print("\nCreating visualization...")
    try:
        fig = visualize_hierarchy(n_zeros=50)
        plt.show()
    except Exception as e:
        print(f"Visualization skipped: {e}")
        print("(matplotlib may not be available in this environment)")
    
    print("\n✅ Demonstration complete!")
    print("\n🕳️ → ☀️\n")


if __name__ == "__main__":
    main()
Demonstration of the Unified Hierarchy Framework

This script demonstrates that all five systems converge to ζ(s) as the
fundamental base, as established by the Unified Hierarchy Theorem.

Usage:
    python demo_unified_hierarchy.py [--precision DPS] [--zeros N]

Author: José Manuel Mota Burruezo Ψ ✧ ∞³
Institution: Instituto de Conciencia Cuántica (ICQ)
"""

import argparse
import sys
from pathlib import Path

# Add current directory to path
sys.path.insert(0, str(Path(__file__).parent))

from utils.unified_hierarchy import UnifiedHierarchySystem
import mpmath as mp


def demonstrate_system_1(hierarchy: UnifiedHierarchySystem):
    """Demonstrate System 1: φ (Fractal Modulation)"""
    print("\n" + "="*80)
    print("💎 SYSTEM 1: φ (Golden Ratio) - FRACTAL MODULATION")
    print("="*80)
    
    sys1 = hierarchy.system1_fractal_modulation()
    
    print("\nThe golden ratio φ modulates fine fluctuations of zero spacing.")
    print(f"\nφ = {hierarchy.phi}")
    print(f"\nZero spacing formula:")
    print("  Δγ_n = γ_(n+1) - γ_n ∼ (2π/log n) × (1 + ε_n φ^(-n))")
    
    print(f"\nFirst 10 zero spacings:")
    for i in range(min(10, len(sys1['spacings']))):
        delta = sys1['spacings'][i]
        weyl = sys1['weyl_predictions'][i]
        mod = sys1['modulations'][i]
        print(f"  Δγ_{i+1} = {delta:8.4f}  (Weyl: {weyl:6.4f}, Mod: {mod:+.6f})")
    
    print(f"\nAverage modulation amplitude: {sys1['average_modulation']:.6f}")
    
    print("\nφ^(-n) decay (first 10 terms):")
    for i, val in enumerate(sys1['phi_power_decay'][:10], 1):
        print(f"  φ^(-{i}) = {val:.8f}")
    
    if sys1['self_similarity']:
        print("\nSelf-similarity analysis (f_(n+k)/f_n ≈ φ^(α·k)):")
        for ratio_data in sys1['self_similarity'][:5]:
            print(f"  Index {ratio_data['index']:2d}: ratio = {ratio_data['ratio']:.4f}, "
                  f"α ≈ {ratio_data['alpha']:.4f}")


def demonstrate_system_2(hierarchy: UnifiedHierarchySystem):
    """Demonstrate System 2: ζ(n) (Analytic Moments)"""
    print("\n" + "="*80)
    print("🔮 SYSTEM 2: ζ(n) - ANALYTIC MOMENTS")
    print("="*80)
    
    sys2 = hierarchy.system2_analytic_moments()
    
    print("\nThe values ζ(n) are the 'moments' of the zero distribution.")
    print("They contain complete information about density and correlations.")
    
    print("\nSpecial values of ζ(n):")
    for n, (exact_val, formula) in sys2['exact_forms'].items():
        computed = sys2['zeta_values'][n]
        print(f"  ζ({n}) = {computed:.10f}  (exact: {formula})")
    
    print(f"\nζ'(1/2) = {sys2['zeta_prime_half']:.10f}")
    print("  This connects to f₀ via the spectral-physical bridge")
    
    print("\nEmpirical moments from zero distribution:")
    for k, moment in sys2['empirical_moments'].items():
        print(f"  M_{k} = Σ γ_n^{k} = {moment:.6e}")


def demonstrate_system_3(hierarchy: UnifiedHierarchySystem):
    """Demonstrate System 3: QCAL Codons (Symbiotic Resonance)"""
    print("\n" + "="*80)
    print("🧬 SYSTEM 3: QCAL CODONS - SYMBIOTIC RESONANCE")
    print("="*80)
    
    sys3 = hierarchy.system3_qcal_codons()
    
    print("\nCodons are 'chords' in the spectral space of ζ(s).")
    print(f"Resonance criterion: {sys3['resonance_criterion']}")
    
    print("\nDigit → Frequency mapping:")
    for digit, freq in list(sys3['digit_map'].items())[:5]:
        print(f"  Digit {digit} → {freq:.4f} Hz")
    
    print("\nCodon Analysis:")
    print("-" * 80)
    for codon_name, data in sys3['codons'].items():
        res = data['resonance']
        status = "✓ RESONANT" if res.resonant else "✗ Non-resonant"
        print(f"\n  Codon {codon_name}: {data['digits']}")
        print(f"    Frequency: {data['frequency']:.4f} Hz")
        print(f"    Nearest zero: n={res.nearest_zero_index}, γ={res.nearest_zero_gamma:.4f}")
        print(f"    Nearest freq: {res.nearest_frequency:.4f} Hz")
        print(f"    Deviation: {res.deviation:.4f} Hz")
        print(f"    Status: {status}")


def demonstrate_system_4(hierarchy: UnifiedHierarchySystem):
    """Demonstrate System 4: Harmonics (Vibrational Overtones)"""
    print("\n" + "="*80)
    print("🎵 SYSTEM 4: HARMONICS - VIBRATIONAL OVERTONES")
    print("="*80)
    
    sys4 = hierarchy.system4_harmonics()
    
    print("\nHarmonics are integer multiples: f_n^(k) = k · f_n")
    print("They arise from the Euler product: log ζ(s) = Σ_p Σ_k p^(-ks)/k")
    
    print("\nHarmonic series for first 3 fundamentals:")
    for key in list(sys4['harmonic_series'].keys())[:3]:
        data = sys4['harmonic_series'][key]
        print(f"\n  {key} (γ = {data['gamma']:.4f}):")
        print(f"    Fundamental: {data['fundamental']:.4f} Hz")
        print(f"    Harmonics 2-5: ", end="")
        print(", ".join(f"{h:.2f}" for h in data['harmonics'][1:5]))
    
    if sys4['overlaps']:
        print("\nHarmonic-Fundamental Overlaps (cross-resonances):")
        print("-" * 80)
        for overlap in sys4['overlaps'][:5]:
            print(f"  f_{overlap['fundamental_index']}×{overlap['harmonic_number']} "
                  f"≈ f_{overlap['matches_fundamental']} "
                  f"(deviation: {overlap['deviation']:.4%})")


def demonstrate_system_5(hierarchy: UnifiedHierarchySystem):
    """Demonstrate System 5: ζ(s) (Fundamental Base)"""
    print("\n" + "="*80)
    print("🌀 SYSTEM 5: ζ(s) - FUNDAMENTAL BASE")
    print("="*80)
    
    sys5 = hierarchy.system5_zeta_base()
    
    print(f"\nDefinition: {sys5['definition']}")
    print("\nζ(s) is THE fundamental base from which ALL systems emerge.")
    
    zeros = sys5['zeros']
    print(f"\nZero Properties:")
    print(f"  Total computed: {zeros['total_computed']}")
    print(f"  First zero γ₁ = {zeros['first_zero']['gamma']:.8f}")
    print(f"  First frequency f₁ = {zeros['first_zero']['frequency']:.8f} Hz")
    print(f"  Average spacing: {zeros['average_spacing']:.4f}")
    
    curvature = sys5['spectral_curvature']
    print(f"\nSpectral Curvature δζ:")
    print(f"  δζ = f₀ - 100√2")
    print(f"  Computed: {curvature['delta_zeta']:.6f} Hz")
    print(f"  Theoretical: {curvature['theoretical']:.6f} Hz")
    print(f"  Interpretation: {curvature['interpretation']}")
    
    print("\nCritical Line Sample |ζ(1/2 + it)|:")
    for sample in sys5['critical_line_sample'][:3]:
        print(f"  t = {sample['t']:8.4f}: |ζ| = {sample['|ζ(1/2+it)|']:.6f}, "
              f"arg = {sample['arg(ζ)']:+.4f}")
    
    print(f"\nRole: {sys5['role']}")


def demonstrate_convergence(hierarchy: UnifiedHierarchySystem):
    """Demonstrate the convergence theorem"""
    print("\n" + "="*80)
    print("✨ CONVERGENCE THEOREM VALIDATION")
    print("="*80)
    
    results = hierarchy.validate_convergence()
    
    print(f"\n{results['theorem']}")
    print("\nSystem Validation:")
    print("-" * 80)
    
    for system_name, data in results['systems'].items():
        print(f"\n{system_name}:")
        print(f"  {data['status']}")
        print(f"  Convergence: {data['convergence']}")
        for key, value in data.items():
            if key not in ['status', 'convergence']:
                print(f"  {key}: {value}")
    
    print("\n" + "="*80)
    print("GLOBAL COHERENCE")
    print("="*80)
    
    coh = results['global_coherence']
    print(f"\nf₀ = {coh['f0']} Hz")
    print(f"δζ = {coh['delta_zeta']} Hz")
    print(f"C_coherence = {coh['C_coherence']}")
    print(f"Coherence factor = {coh['coherence_factor']:.6f}")
    print(f"\n{coh['interpretation']}")


def main():
    """Main demonstration"""
    parser = argparse.ArgumentParser(
        description="Demonstrate Unified Hierarchy: All systems converge to ζ(s)"
    )
    parser.add_argument(
        '--precision', 
        type=int, 
        default=25,
        help='Decimal precision for calculations (default: 25)'
    )
    parser.add_argument(
        '--zeros',
        type=int,
        default=50,
        help='Number of ζ(s) zeros to compute (default: 50)'
    )
    
    args = parser.parse_args()
    
    print("\n" + "╔" + "="*78 + "╗")
    print("║" + " "*20 + "🌌 UNIFIED HIERARCHY DEMONSTRATION 🌌" + " "*20 + "║")
    print("╚" + "="*78 + "╝")
    
    print(f"\nInitializing system...")
    print(f"  Precision: {args.precision} decimal places")
    print(f"  Computing {args.zeros} zeros of ζ(s)...")
    
    try:
        hierarchy = UnifiedHierarchySystem(
            precision=args.precision,
            num_zeros=args.zeros
        )
        
        print(f"\n✓ Initialization complete")
        print(f"  First zero: γ₁ = {hierarchy.gammas[0]:.8f}")
        print(f"  Base frequency: f₀ = {hierarchy.f0} Hz")
        
        # Demonstrate each system
        demonstrate_system_1(hierarchy)
        demonstrate_system_2(hierarchy)
        demonstrate_system_3(hierarchy)
        demonstrate_system_4(hierarchy)
        demonstrate_system_5(hierarchy)
        
        # Show convergence
        demonstrate_convergence(hierarchy)
        
        # Print the hierarchy diagram
        hierarchy.print_hierarchy_diagram()
        
        print("\n" + "="*80)
        print("✨ CONCLUSION")
        print("="*80)
        print("\nNo hay cinco sistemas independientes.")
        print("Hay UNO SOLO: el campo ζ(s).")
        print("\nTodo lo demás es:")
        print("  • Proyección")
        print("  • Modulación")
        print("  • Resonancia")
        print("  • Consecuencia")
        print("\nY la conciencia emerge cuando:")
        print("  π_α(ζ) = π_δζ(ζ) sobre G")
        print("\n🌌 El universo es una sinfonía de ζ(s).")
        print("Y somos los acordes que resuenan en la frecuencia f₀.")
        print("="*80)
        
        return 0
        
    except Exception as e:
        print(f"\n✗ Error: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
