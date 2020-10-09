// Copyright (c) 2015-2020 Clearmatics Technologies Ltd
//
// SPDX-License-Identifier: LGPL-3.0+

pragma solidity ^ 0.5.0;

import "./bls12_377_groth16.sol";

contract bls12_377_groth16_test
{
    uint256[] _vk;

    function test_verify(
        uint256[] memory vk,
        uint256[0x10] memory proof,
        uint256[] memory inputs) public returns(bool)
    {
        _vk = vk;
        return bls12_377_groth16.verify(_vk, proof, inputs);
    }
}
