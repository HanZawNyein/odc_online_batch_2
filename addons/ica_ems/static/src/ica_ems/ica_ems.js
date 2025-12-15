import {registry} from "@web/core/registry";

import {Component, useState} from "@odoo/owl";
import {ResPartnerComponent} from "./components/res_partner/res_partner";

class EmsClientAction extends Component {
    static template = "ica_ems.emsClientAction";
    static components = {ResPartnerComponent};

    setup() {
        this.state = useState({
            count: 0,
        });
    }

    addCount() {
        this.state.count++;
        console.log(this.state.count)
    }

    removeCount() {
        if (this.state.count > 0) {
            this.state.count--;
        }
    }
}

// remember the tag name we put in the first step
registry.category("actions").add("ica_ems.emsClientAction", EmsClientAction);