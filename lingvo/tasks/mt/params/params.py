# Lint as: python3
# Copyright 2018 The TensorFlow Authors. All Rights Reserved.
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
# ==============================================================================
"""Machine translation model hyper-parameters."""

# Import ModelParams to ensure that they are added to the global registry.
# pylint: disable=unused-import
import lingvo.tasks.mt.params.wmt14_en_de
import lingvo.tasks.mt.params.wmtm16_en_de
import lingvo.tasks.mt.params.xendec.wmt14_en_de

# pylint: enable=unused-import
