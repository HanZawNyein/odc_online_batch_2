import {Component, onWillStart, useState, useRef} from "@odoo/owl";
import {useService} from "@web/core/utils/hooks";

export class ResPartnerComponent extends Component {
    static template = "ica_ems.ResPartnerComponent";
    static props = {
        partners: Array,
        fetchPartners: Function,
        createPartner: Function,
    }

    setup() {
        this.searchRef = useRef('search');
        this.state = useState({
            currentPartner: {
                id: null,
                name: null,
                date_of_birth: null,
            }
        })
    }

    async searchPartners() {
        let value = this.searchRef.el.value;
        let domain = [];
        if (value) {
            domain = [['name', 'ilike', value]]
        }
        await this.props.fetchPartners(domain)
        this.searchRef.el.value = '';
    }

    async createPartner() {
        // console.log()
        let result = await this.props.createPartner(this.state.currentPartner);
        if (result) {
            this.removeCurrentPartner();
        }

        // console.log("I am res partner component.")
    }

    updatePartner(activePartner) {
        this.state.currentPartner = {...activePartner, name: activePartner.display_name};
        // console.log(activePartner)
    }

    removeCurrentPartner() {
        // console.log("removeCurrentPartner")
        this.state.currentPartner = {
            id: null,
            name: null,
            date_of_birth: null,
        }
    }
}