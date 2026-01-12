import {ProductCard} from "@point_of_sale/app/components/product_card/product_card";
import {patch} from "@web/core/utils/patch";
import {useState, onWillStart} from "@odoo/owl";
import {useService} from "@web/core/utils/hooks";

patch(ProductCard.prototype, {
    setup() {
        super.setup(...arguments)
        this.ormService = useService('orm');
        this.state = useState(
            {productQty: 0.0,}
        );
        onWillStart(async () => {
            await this.getQuantity()
        })
    },
    async getQuantity() {
        if (this.props.productId !== undefined) {
            let result = await this.ormService.searchRead('product.template', [['id', '=', this.props.productId]], ['qty_available']);
            this.state.productQty = result[0]?result[0]['qty_available']:'0.0';
        }
    }
})