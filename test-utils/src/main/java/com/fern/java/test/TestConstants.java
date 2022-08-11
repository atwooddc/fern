/*
 * (c) Copyright 2022 Birch Solutions Inc. All rights reserved.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package com.fern.java.test;

import com.fern.codegen.GeneratorContext;
import com.fern.types.FernConstants;
import java.util.Collections;

public final class TestConstants {

    public static final String PACKAGE_PREFIX = "com";

    public static final FernConstants FERN_CONSTANTS = FernConstants.builder()
            .errorDiscriminant("_error")
            .unknownErrorDiscriminantValue("_unknown")
            .errorInstanceIdKey("_errorInstanceId")
            .build();

    public static final GeneratorContext GENERATOR_CONTEXT =
            new GeneratorContext(PACKAGE_PREFIX, Collections.emptyMap(), Collections.emptyMap(), FERN_CONSTANTS);

    private TestConstants() {}
}
