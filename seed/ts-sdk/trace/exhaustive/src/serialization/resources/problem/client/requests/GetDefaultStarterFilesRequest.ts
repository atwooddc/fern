/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../../../../index";
import * as SeedTrace from "../../../../../api/index";
import * as core from "../../../../../core";
import { VariableTypeAndName } from "../../types/VariableTypeAndName";

export const GetDefaultStarterFilesRequest: core.serialization.Schema<
    serializers.GetDefaultStarterFilesRequest.Raw,
    SeedTrace.GetDefaultStarterFilesRequest
> = core.serialization.object({
    inputParams: core.serialization.list(VariableTypeAndName),
    outputType: core.serialization.lazy(async () => (await import("../../../..")).VariableType),
    methodName: core.serialization.string(),
});

export declare namespace GetDefaultStarterFilesRequest {
    interface Raw {
        inputParams: VariableTypeAndName.Raw[];
        outputType: serializers.VariableType.Raw;
        methodName: string;
    }
}
