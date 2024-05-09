/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../../../../index";
import * as SeedMultiLineDocs from "../../../../../api/index";
import * as core from "../../../../../core";

export const CreateUserRequest: core.serialization.Schema<
    serializers.CreateUserRequest.Raw,
    SeedMultiLineDocs.CreateUserRequest
> = core.serialization.object({
    name: core.serialization.string(),
    age: core.serialization.number().optional(),
});

export declare namespace CreateUserRequest {
    interface Raw {
        name: string;
        age?: number | null;
    }
}