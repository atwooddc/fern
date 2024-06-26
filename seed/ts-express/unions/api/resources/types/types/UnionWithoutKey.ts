/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as SeedUnions from "../../../index";

export type UnionWithoutKey =
    | SeedUnions.UnionWithoutKey.Foo
    /**
     * This is a bar field. */
    | SeedUnions.UnionWithoutKey.Bar;

export declare namespace UnionWithoutKey {
    interface Foo extends SeedUnions.Foo {
        type: "foo";
    }

    interface Bar extends SeedUnions.Bar {
        type: "bar";
    }
}
