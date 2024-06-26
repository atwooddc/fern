/**
 * This file was auto-generated by Fern from our API Definition.
 */

/**
 * @example
 *     {
 *         limit: 1,
 *         otherField: "string",
 *         multiLineDocs: "string",
 *         optionalMultipleField: "string",
 *         multipleField: "string"
 *     }
 */
export interface GetPlaylistsRequest {
    limit?: number;
    /**
     * i'm another field
     */
    otherField: string;
    /**
     * I'm a multiline
     * description
     */
    multiLineDocs: string;
    optionalMultipleField?: string | string[];
    multipleField: string | string[];
}
