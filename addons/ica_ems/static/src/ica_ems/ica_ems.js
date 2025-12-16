import {registry} from "@web/core/registry";

import {Component, onWillStart, useState} from "@odoo/owl";
import {useService} from "@web/core/utils/hooks";
import {Layout} from "@web/search/layout";

import {ResPartnerComponent} from "./components/res_partner/res_partner";

class EmsClientAction extends Component {
    static template = "ica_ems.emsClientAction";
    static components = {ResPartnerComponent, Layout};

    setup() {
        this.state = useState({
            // count: 0,
            partners: [],
        });
        this.ormService = useService('orm');

        onWillStart(async () => {
            await this.fetchPartners();
        })
    }

    async fetchPartners(domain = []) {
        this.state.partners = await this.ormService.searchRead('res.partner', domain,
            ['display_name', 'age', 'date_of_birth'],
            {limit: 10, offset: 0, order: 'id desc'});
        // console.log(this.state.partners)
    }

    async createPartner(values) {
        console.log(values);
        let partners = {}
        if (values.id) {
            //     write
            partners= await this.ormService.write('res.partner', [values.id],{...values});
        } else {
            console.log("i am from ica_ems component");
            partners =  await this.ormService.create('res.partner', [{...values}]);
            // console.log(newPartner)
        }
        await this.fetchPartners();
        return partners;
    }
}

// remember the tag name we put in the first step
registry.category("actions").add("ica_ems.emsClientAction", EmsClientAction);