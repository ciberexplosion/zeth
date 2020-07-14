// Copyright (c) 2015-2020 Clearmatics Technologies Ltd
//
// SPDX-License-Identifier: LGPL-3.0+

#include "libzeth/circuits/circuit_types.hpp"
#include "libzeth/circuits/circuit_wrapper.hpp"
#include "mpc_common.hpp"
#include "zeth_config.h"

void zeth_protoboard(libsnark::protoboard<FieldT> &pb)
{
    libzeth::joinsplit_gadget<
        FieldT,
        libzeth::HashT<FieldT>,
        libzeth::HashTreeT<FieldT>,
        libzeth::ZETH_NUM_JS_INPUTS,
        libzeth::ZETH_NUM_JS_OUTPUTS,
        libzeth::ZETH_MERKLE_TREE_DEPTH>
        js(pb);
    js.generate_r1cs_constraints();
}

int main(int argc, char **argv)
{
    const std::map<std::string, subcommand *> commands{
        {"linear-combination", mpc_linear_combination_cmd},
        {"dummy-phase2", mpc_dummy_phase2_cmd},
        {"phase2-begin", mpc_phase2_begin_cmd},
        {"phase2-contribute", mpc_phase2_contribute_cmd},
        {"phase2-verify-contribution", mpc_phase2_verify_contribution_cmd},
        {"phase2-verify-transcript", mpc_phase2_verify_transcript_cmd},
        {"create-keypair", mpc_create_keypair_cmd},
    };
    return mpc_main(argc, argv, commands, zeth_protoboard);
}
