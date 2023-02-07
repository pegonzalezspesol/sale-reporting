/** @odoo-module **/

import {SectionAndNoteListRenderer} from "@account/components/section_and_note_fields_backend/section_and_note_fields_backend";
import {patch} from "@web/core/utils/patch";

patch(SectionAndNoteListRenderer.prototype, "sale_layout_category_hide_detail", {
    getCellClass(column, record) {
        const classNames = this._super(...arguments);
        if (this.isSectionOrNote(record) && column.widget === "boolean_fa_icon") {
            return classNames.replace(" o_hidden", "");
        }
        return classNames;
    },

    getSectionColumns(columns) {
        const sectionCols = columns.filter(
            (col) =>
                ["handle", "boolean_fa_icon"].includes(col.widget) ||
                (col.type === "field" && col.name === this.titleField)
        );
        return sectionCols.map((col) => {
            if (col.name === this.titleField) {
                return {...col, colspan: columns.length - sectionCols.length + 1};
            }
            return {...col};
        });
    },
});
