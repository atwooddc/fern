/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../../../../../index";
import * as core from "../../../../../../core";

export const NotFoundError: core.serialization.Schema<serializers.folder.NotFoundError.Raw, string> =
    core.serialization.string();

export declare namespace NotFoundError {
    type Raw = string;
}
