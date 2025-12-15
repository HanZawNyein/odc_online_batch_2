import {Component, onWillStart, useState, useRef} from "@odoo/owl";
import {useService} from "@web/core/utils/hooks";

export class ResPartnerComponent extends Component {
    static template = "ica_ems.ResPartnerComponent";

    setup() {
        this.searchRef = useRef('search');
        this.state = useState({
            partners: [],
        });
        this.ormService = useService('orm');

        onWillStart(async () => {
            await this.fetchPartners()
        })
    }

    async fetchPartners(domain=[]) {
        this.state.partners = await this.ormService.searchRead('res.partner', domain, ['display_name', 'age', 'date_of_birth']);
        // console.log(this.state.partners)
    }

    async searchPartners() {
        let value = this.searchRef.el.value;
        // console.log(typeof value)
        // console.log(value)
        let domain = [];
        if (value) {
            domain = [['display_name', 'ilike', value]]
        }
        await this.fetchPartners(domain)
        this.searchRef.el.value = '';
    }
}