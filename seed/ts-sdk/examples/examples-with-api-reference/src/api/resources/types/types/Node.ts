/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as SeedExamples from "../../../index";

/**
 * @example
 *     {
 *         name: "root",
 *         nodes: [{
 *                 name: "left"
 *             }, {
 *                 name: "right"
 *             }],
 *         trees: [{
 *                 nodes: [{
 *                         name: "left"
 *                     }, {
 *                         name: "right"
 *                     }]
 *             }]
 *     }
 *
 * @example
 *     {
 *         name: "left"
 *     }
 *
 * @example
 *     {
 *         name: "right"
 *     }
 */
export interface Node {
    name: string;
    nodes?: SeedExamples.Node[];
    trees?: SeedExamples.Tree[];
}
