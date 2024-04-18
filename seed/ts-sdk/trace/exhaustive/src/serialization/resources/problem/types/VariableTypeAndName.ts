/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../../../index";
import * as SeedTrace from "../../../../api/index";
import * as core from "../../../../core";

export const VariableTypeAndName: core.serialization.ObjectSchema<
    serializers.VariableTypeAndName.Raw,
    SeedTrace.VariableTypeAndName
> = core.serialization.object({
    variableType: core.serialization.lazy(async () => (await import("../../..")).VariableType),
    name: core.serialization.string(),
});

export declare namespace VariableTypeAndName {
    interface Raw {
        variableType: serializers.VariableType.Raw;
        name: string;
    }
}
