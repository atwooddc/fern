/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../../../index";
import * as SeedMixedCase from "../../../../api/index";
import * as core from "../../../../core";
import { User } from "./User";

export const NestedUser: core.serialization.ObjectSchema<serializers.NestedUser.Raw, SeedMixedCase.NestedUser> =
    core.serialization.object({
        Name: core.serialization.string(),
        NestedUser: User,
    });

export declare namespace NestedUser {
    interface Raw {
        Name: string;
        NestedUser: User.Raw;
    }
}
