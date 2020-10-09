// Copyright (c) 2015-2020 Clearmatics Technologies Ltd
//
// SPDX-License-Identifier: LGPL-3.0+

pragma solidity ^0.5.0;

library bls12_377_groth16
{
    // "nested_pairing_parameters": {
    //   "r": "12ab655e9a2ca55660b44d1e5c37b00159aa76fed00000010a11800000000001",
    //   "q": "01ae3a4617c510eac63b05c06ca1493b1a22d9f300f5138f1ef3622fba094800170b5d44300000008508c00000000001",
    //   "generator_g1": [
    //     "0x008848defe740a67c8fc6225bf87ff5485951e2caa9d41bb188282c8bd37cb5cd5481512ffcd394eeab9b16eb21be9ef",
    //     "0x01914a69c5102eff1f674f5d30afeec4bd7fb348ca3e52d96d182ad44fb82305c2fe3d3634a9591afd82de55559c8ea6"
    //   ],
    //   "generator_g2": [
    //     ["0x00d6ac33b84947d9845f81a57a136bfa326e915fabc8cd6a57ff133b42d00f62e4e1af460228cd5184deae976fa62596",
    //      "0x00b997fef930828fe1b9e6a1707b8aa508a3dbfd7fe2246499c709226a0a6fef49f85b3a375363f4f8f6ea3fbd159f8a"],
    //     ["0x0185067c6ca76d992f064a432bd9f9be832b0cac2d824d0518f77d39e76c3e146afb825f2092218d038867d7f337a010",
    //      "0x0118dd509b2e9a13744a507d515a595dbb7e3b63df568866473790184bdf83636c94df2b7a962cb2af4337f07cb7e622"]
    //   ]
    // }

    // Fr elements occupy 1 uint256, and Fq elements occupy 2 uint256s.
    // Therefore G1 elements occupy 4 uint256s. G2 elements have coordinates in
    // Fp2, and thus occupy 8 uint256s.
    //
    // Note that there is scope for compacting 2 Fq elements into 3 uint256s.
    // For now, this is not done, and the precompiled contracts used here do
    // not support it.

    // VerifyingKey:
    //     uint256[4] Alpha;       // slots 0x00
    //     uint256[8] Minus_Beta;  // slots 0x04
    //     uint256[8] Minus_Delta; // slots 0x0c
    //     uint256[] ABC;          // slots 0x14

    // Proof:
    //
    //     uint256[4] a,           // offset 0x00 (0x000 bytes)
    //     uint256[8] b,           // offset 0x04 (0x080 bytes)
    //     uint256[4] c,           // offset 0x0c (0x180 bytes)
    //     <end>                   // offset 0x10 (0x200 bytes)

    // Return the value r, the characteristic of the scalar field.
    function scalar_r() internal pure returns(uint256)
    {
        return 0x12ab655e9a2ca55660b44d1e5c37b00159aa76fed00000010a11800000000001;
    }

    function verify(
        uint256[] storage vk,
        uint256[0x10] memory proof,
        uint256[] memory input) internal returns (bool)
    {
        return 0 < vk.length + proof.length + input.length;
    }
}
