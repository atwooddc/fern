/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../../../../../index";
import * as SeedTrace from "../../../../../../api/index";
import * as core from "../../../../../../core";
import { Language } from "../../../../commons/types/Language";

export const GetFunctionSignatureResponse: core.serialization.ObjectSchema<
    serializers.v2.GetFunctionSignatureResponse.Raw,
    SeedTrace.v2.GetFunctionSignatureResponse
> = core.serialization.object({
    functionByLanguage: core.serialization.record(Language, core.serialization.string().optional()),
});

export declare namespace GetFunctionSignatureResponse {
    interface Raw {
        functionByLanguage: Record<Language.Raw, string | null | undefined>;
    }
}
