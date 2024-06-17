/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as FernDocsConfig from "../../..";

export interface ApiReferenceSectionConfiguration {
    /** The title of the api package that will be displayed in the sidebar. */
    section: string;
    /** This section will inherit the endpoints from the specified subpackage(s). If multiple packages are specified, they will be merged. */
    referencedPackages?: string[];
    /** Relative path to the markdown file. */
    summary?: string;
    contents?: FernDocsConfig.ApiReferenceLayoutItem[];
    slug?: string;
    icon?: string;
    hidden?: boolean;
    skipSlug?: boolean;
}
