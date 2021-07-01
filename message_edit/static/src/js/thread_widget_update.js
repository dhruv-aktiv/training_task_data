odoo.define('message_edit.thread_widget_update', function(require) {
    "use strict";

    // console.log("Hello World!!!");

    // alert("js called !!!");


    var ThreadWidget = require('mail.widget.Thread');
    var core = require('web.core');

    var QWeb = core.qweb;

    ThreadWidget.include({
        events: _.extend({}, ThreadWidget.prototype.events, {
            'click .o_thread_edit': '_onClickEditMsg'
        }),

     init: function () {
        this._super.apply(this, arguments);
    
        },
    
        render: function (thread, options) {
            this._super.apply(this, arguments);
        
        },

     _onClickEditMsg: function (ev) {
        var messageID = $(ev.currentTarget).data('message-id');
      
        console.log

       // $(ev.currentTarget).parent();

        console.log($($($(ev.currentTarget).parent()).parent()).parent().data('message-id'));


        console.log("on clicked!!!");
        console.log(`messageID : ${messageID}`);
  



         

               



  // self.do_action({
  //                   type:'ir.actions.act_window',
  //                   res_id: id,
  //                   res_model: self.modelName,
  //                   views: [[viewId || false, 'form']],
  //                   target: 'current',
  //                   context: event.context || self.context,
  //               });
  //           });
  //           return;



        // var action = {
        //     type: "ir.actions.act_window",
        //     name: "Message/Note Edit",
        //     res_model: "mail.message",
        //     target: 'new',
        //     views: [
        //     ['false', 'form']
        //     ],
        //     view_type: 'form',
        //     view_mode: 'form',
        //     res_id : messageID,
        //     context: {
        //     // default_shipment_type: values[0][1][0],
        //     // default_shipments_packing_ids: pack_list,
        //     },
        //     flags: {
        //     'form': {
        //     'action_buttons': true,
        //     'options': {
        //     'mode': 'edit'
        //     }
        //     }
        //     }
        // };
        // return this.do_action(action);  

        // this.do_action('message_edit.message_note_edit_action', {
        //     additional_context: {
        //         'default_res_id' : messageID
        //     },
           
        // });
      console.log("Msg Edited Wizard opened successfully...");

       this._rpc({
                    model: 'ir.model.data',
                    method: 'get_object_reference',
                    args: ['message_edit', 'message_note_edit_action'],
            }).then(function (data) {
                   
                     this.do_action({
                    type:'ir.actions.act_window',
                    res_id: messageID,
                    res_model: "mail.message",
                    views: [['form']],
                    target: 'new',
                });
                    
                });
    },

    });

});