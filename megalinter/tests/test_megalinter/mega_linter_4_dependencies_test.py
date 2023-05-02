#!/usr/bin/env python3
"""
Unit tests for Megalinter class

"""
import os
import unittest
import uuid

import megalinter
from megalinter import utilstest
from megalinter.constants import DEFAULT_DOCKER_WORKSPACE_DIR, ML_REPO


class mega_linter_4_dependencies_test(unittest.TestCase):
    def __init__(self, args) -> None:
        self.request_id = str(uuid.uuid1())
        super().__init__(args)

    def setUp(self):
        utilstest.linter_test_setup(
            {
                "request_id": self.request_id,
                "sub_lint_root": f"{os.path.sep}.automation{os.path.sep}test{os.path.sep}dependencies",
            }
        )

    def test_override_cli_executable(self):
        mega_linter, output = utilstest.call_mega_linter(
            {
                "ENABLE_LINTERS": "TYPESCRIPT_ES",
                "TYPESCRIPT_ES_CLI_EXECUTABLE": ["yarn", "run", "eslint"],
                "PRINT_ALL_FILES": "false",
                "MEGALINTER_FLAVOR": "javascript",
                "FLAVOR_SUGGESTIONS": "false",
                "TYPESCRIPT_ES_PRE_COMMANDS": [
                    {
                        "command": "npm install @tsconfig/node18-strictest-esm@1.0.1",
                        "continue_if_failed": False,
                        "cwd": "workspace",
                    }
                ],
                "request_id": self.request_id,
            }
        )
        self.assertTrue(
            len(mega_linter.linters) > 0, "Linters have been created and run"
        )
        self.assertIn("- Number of files analyzed", output)