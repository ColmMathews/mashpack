# Copyright 2018 Seth Michael Larson
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import pytest
from mashpack._fallback import (
    Unpacker as PythonUnpacker, Packer as PythonPacker
)


@pytest.fixture(scope='session')
def packer_type():
    if os.environ.get('TEST_WITH_CYTHON') == 'true':
        raise NotImplementedError()
    else:
        return PythonPacker


@pytest.fixture(scope='session')
def packer_type():
    if os.environ.get('TEST_WITH_CYTHON') == 'true':
        raise NotImplementedError()
    else:
        return PythonUnpacker


@pytest.fixture(scope='test')
def unpacker(unpacker_type):
    return unpacker_type()


@pytest.fixture(scope='test')
def packer(packer_type):
    return packer_type()
