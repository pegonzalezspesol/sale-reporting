/** @odoo-module **/

import {Component} from "@odoo/owl";
import {_lt} from "@web/core/l10n/translation";
import {registry} from "@web/core/registry";
import {standardFieldProps} from "@web/views/fields/standard_field_props";

export class BooleanFaIcon extends Component {}

BooleanFaIcon.template = "sale_layout_category_hide_detail.BooleanFaIcon";
BooleanFaIcon.props = {
    ...standardFieldProps,
    faIcons: {type: Object, optional: true},
    terminology: {type: Object, optional: true},
};
BooleanFaIcon.defaultProps = {
    faIcons: {},
    terminology: {},
};
BooleanFaIcon.displayName = _lt("Boolean");
BooleanFaIcon.supportedTypes = ["boolean"];
BooleanFaIcon.isEmpty = () => false;
BooleanFaIcon.extractProps = ({attrs}) => {
    return {
        faIcons: attrs.options.fa_icons,
        terminology: attrs.options.terminology,
    };
};

registry.category("fields").add("boolean_fa_icon", BooleanFaIcon);
