# Copyright (c) 2015-2020 Clearmatics Technologies Ltd
#
# SPDX-License-Identifier: LGPL-3.0+

from zeth.core import zksnark
from zeth.api import ec_group_messages_pb2
import json
from unittest import TestCase


class TestZKSnark(TestCase):

    def test_g1_proto_encode_decode(self) -> None:
        self._do_test_g1_proto_encode_decode(("0xaabbccdd", "0x11223344"))

    def test_g2_proto_encode_decode(self) -> None:
        self._do_test_g2_proto_encode_decode(("0xaabbccdd", "0x11223344"))
        self._do_test_g2_proto_encode_decode(
            (("0xcdeeff00", "0x11223344"), ("0x55667788", "0x99aabbcc")))

    def test_groth16_verification_key_proto_encode_decode(self) -> None:
        # pylint: disable=line-too-long
        vk_1 = {
            "alpha": [
                "0x009d7309d79d5215384a7a9a1d9372af909582781f388a51cb833c87b8024519cf5b343cb35d49a5aa52940f14b7b8e7",  # noqa
                "0x012816ef6069ef1e40eaab0a111f9b98b276dbf2a3209d788eb8ce635ce92a29c2bcdaa3bb9b375a8d3ee4325c07f4ea"  # noqa
            ],
            "beta": [
                [
                    "0x017abb9470ccb0ef09676df87dbe181a9ed89ba1cf1e32a2031d308b4c11a84fd97ac202fb82264cec178e22b71598b9",  # noqa
                    "0x01774daba40ce4c9fe2d2c6d17a3821b31ec63a77ebea2dab8b3218fd7eb90f9d561d87ab9712f3bafcf30ed3676553b"  # noqa
                ],
                [
                    "0x00ce3769d0c1e29aa799a5928b1c524a5a85326c4b16463530bfdcab82f55ef6c4649d4916e3c6e5eebd1f8c932b7be1",  # noqa
                    "0x009234f3340fb85ae722ed052b8dcf63193c423791d9c43ab725a35286bda1708c3a9d8bff4c1fd55d981c10a30e9cff"  # noqa
                ]
            ],
            "delta": [
                [
                    "0x00c19b1795e634573c0514de0cea5bd05d88c24b08aeadc03ec4686ee6741b80e7dea9065d654a3b703ac8e43173f909",  # noqa
                    "0x01a00d16c4d2805e248debf48ea0771e627e2bfb95198df0cbe09a1eb4879fe5fae208347a21c113061921b6a84f7e7d"  # noqa
                ],
                [
                    "0x00361ca07388d760898e0969f3b9a3d6d751b83d770007761e1c5cc798852ed89007ee1504d7c6c7a398693100eef416",  # noqa
                    "0x009a7d27c8392eefe1ba23a52d509cda59ba3c5acc95765d1146a998c780277fb318e47a4e4a554d8a3e6f56ccdd2566"  # noqa
                ]
            ],
            "ABC": [
                [
                    "0x001098a772e5fb9edbbd68943000e46bb0f3f2514cbbe1ef15ba485d1c07a683674b5b9398270c1ddf640d345f008353",  # noqa
                    "0x018a94eefa95142069e1f1c069d48645201d1201bc0b7d9bc25ee65a25602362fd237f2168b3c9ca0cabd255088312f5"  # noqa
                ],
                [
                    "0x01a4cfba533c731398e06458003ef7c3920dd1a545b469cc0c35dc19c51942c1531b1b9b395c858ee5b381841fc0001c",  # noqa
                    "0x006194ebb25bab4d163005b23e9cf9aa8d43d242a7792f0fcf269549b46bcc2172443d09bbe573cb5eba60c9c97737c6"  # noqa
                ]
            ]
        }
        # pylint: enable=line-too-long

        self._do_test_verification_key_proto_encode_decode(
            vk_1, zksnark.Groth16SnarkProvider())

    def test_groth16_proof_proto_encode_decode(self) -> None:
        # pylint: disable=line-too-long
        extproof_1 = {
            "proof": {
                "a": [
                    "0x010bd3c06ed5aeb1a7b0653ba63f413b27ba7fd1b77cb4a403fb15f9fb8735abda93a3c78ad05afd111ea68d016cf99e",  # noqa
                    "0x00255a73b1247dcfd62171b29ddbd271cdb7e98b78912ddf6bfe4723cd229f414f9a47cecd0fec7fb74bf13b22a7395b"  # noqa
                ],
                "b": [
                    [
                        "0x01ada9239a53b094ae15473baaa3649afb46d5330f36f8590df668167dd02aaf0a18602ce42654c3d857c4e5e454ca28",  # noqa
                        "0x00938ce5525864aa135674b048bb68adadfabca2a4cea43ea13b19cacec1ae171986009e916f729a085c04cbe22c4127"  # noqa
                    ],
                    [
                        "0x01015a4ea0daaaf8ef20b37c4bda03c2d381be797ae59b621b841d3e61495cf2aaf7e008565884f1d7245ea003ebbf79",  # noqa
                        "0x0128d64383293780f481278fbb22ce1078d79180193361869d9e8639f028ac4c3a7c12f8bc7f7c138821bccd71abcca5"  # noqa
                    ]
                ],
                "c": [
                    "0x00001c5d91872102ab1ca71b321f5e3b6aca698be9d8b432b8f1fc60c37bda88d6f9fdcc91225dd2d17bc58f08826e68",  # noqa
                    "0x000b34a2d07bba78abf1c3e909b1f691bb02f62991a6c6bab53c016e191ecf7929f866eef5231e7f0d29944166a49bf1"  # noqa
                ]
            },
            "inputs": [
                "0x0000000000000000000000000000000000000000000000000000000000000007"  # noqa
            ]
        }
        # pylint: enable=line-too-long
        self._do_test_proof_proto_encode_decode(
            extproof_1, zksnark.Groth16SnarkProvider())

    def _do_test_g1_proto_encode_decode(self, g1: zksnark.GenericG1Point) -> None:
        g1_proto = ec_group_messages_pb2.HexPointBaseGroup1Affine()
        zksnark.group_point_g1_to_proto(g1, g1_proto)
        g1_decoded = zksnark.group_point_g1_from_proto(g1_proto)
        self.assertEqual(g1, g1_decoded)

    def _do_test_g2_proto_encode_decode(self, g2: zksnark.GenericG2Point) -> None:
        g2_proto = ec_group_messages_pb2.HexPointBaseGroup2Affine()
        zksnark.group_point_g2_to_proto(g2, g2_proto)
        g2_decoded = zksnark.group_point_g2_from_proto(g2_proto)
        self.assertEqual(g2, g2_decoded)

    def _do_test_verification_key_proto_encode_decode(
            self,
            vk: zksnark.GenericVerificationKey,
            snark: zksnark.IZKSnarkProvider) -> None:
        vk_proto = snark.verification_key_to_proto(vk)
        vk_decoded = snark.verification_key_from_proto(vk_proto)
        # For now, compare as json to brush over tuple-list differences.
        self.assertEqual(json.dumps(vk), json.dumps(vk_decoded))

    def _do_test_proof_proto_encode_decode(
            self,
            proof: zksnark.GenericProof,
            snark: zksnark.IZKSnarkProvider) -> None:
        proof_proto = snark.proof_to_proto(proof)
        proof_decoded = snark.proof_from_proto(proof_proto)
        self.assertEqual(json.dumps(proof), json.dumps(proof_decoded))
