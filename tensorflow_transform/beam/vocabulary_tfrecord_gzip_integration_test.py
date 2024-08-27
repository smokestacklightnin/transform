#
# Copyright 2020 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Tests for tfrecord_gzip tft.vocabulary and tft.compute_and_apply_vocabulary."""


import pytest
from tensorflow_transform.beam import vocabulary_integration_test
from tensorflow_transform.beam import tft_unit


@pytest.mark.xfail(reason="PR 315 This class contains tests that fail and needs to be fixed. "
"If all tests pass, please remove this mark.")
class TFRecordVocabularyIntegrationTest(
    vocabulary_integration_test.VocabularyIntegrationTest):

  def _VocabFormat(self):
    return 'tfrecord_gzip'


