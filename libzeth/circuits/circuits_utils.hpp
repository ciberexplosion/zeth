// Copyright (c) 2015-2020 Clearmatics Technologies Ltd
//
// SPDX-License-Identifier: LGPL-3.0+

#ifndef __ZETH_CIRCUITS_CIRCUITS_UTILS_HPP__
#define __ZETH_CIRCUITS_CIRCUITS_UTILS_HPP__

#include "libzeth/types/bits.hpp"

#include <libsnark/gadgetlib1/pb_variable.hpp>

namespace libzeth
{

template<typename T> std::vector<bool> convert_to_binary_LE(T x, int bitlen);
std::vector<bool> convert_to_binary(size_t n);

template<typename T> T swap_endianness_u64(T v);
template<typename FieldT>
libsnark::linear_combination<FieldT> packed_addition(
    libsnark::pb_variable_array<FieldT> input);
template<typename FieldT>
libsnark::pb_variable_array<FieldT> from_bits(
    std::vector<bool> bits, const libsnark::pb_variable<FieldT> &ZERO);
void insert_bits256(std::vector<bool> &into, bits256 from);
void insert_bits64(std::vector<bool> &into, bits64 from);
std::vector<unsigned long> bit_list_to_ints(
    std::vector<bool> bit_list, const size_t wordsize);

} // namespace libzeth
#include "libzeth/circuits/circuits_utils.tcc"

#endif // __ZETH_CIRCUITS_CIRCUITS_UTILS_HPP__