var mandrill = require("mandrill-api/mandrill");

mandrill_client = new mandrill.Mandrill("API_KEY");
var template_name = "anomaly-alert";
var template_content = [];
var merge_vars = [
  {
    name: "MAINCONTENT",
    content: "<h1>Facebook_fb_spend</h1><h1>last 15 days Avg. = 2633.88</h1>"
  },
  {
    name: "VISUALS",
    content:
      "<img src='?ui=2&amp;ik=5c0deb2486&amp;view=fimg&amp;th=1646fa8252794773&amp;attid=0.2&amp;disp=emb&amp;realattid=cef73acc1c777565_0.1.1&amp;attbid=ANGjdJ8fo25tRcXez3xejvZ-zp0cE8Lw1EHVpvNu7vwyzMf0R8QkFD6rhbH2UEc2prf9xPcS9_gL6VKVAGTrEVulp8vZjp41-6H04Fhze2p89AH2SU2oAXwTly9CUXQ&amp;sz=s0-l75-ft&amp;ats=1532496034416&amp;rm=1646fa8252794773&amp;zw&amp;atsh=1' alt='Facebook_fb_impressions' class='CToWUd a6T' tabindex='0' width='100%' height='100%'>"
  }
];
mandrill_client.templates.render(
  {
    template_name: template_name,
    template_content: template_content,
    merge_vars: merge_vars
  },
  function(result) {
    sendMail(result);
  },
  function(e) {
    console.log("A mandrill error occurred: " + e.name + " - " + e.message);
  }
);

function sendMail(result) {
  var message = {
    html: result.html,
    text: "Test email template text content",
    subject: "Test email template",
    from_email: "support@clarisights.com",
    from_name: "Clarisights",
    to: [
      {
        email: "yash.arora@adwyze.com",
        name: "Yash Arora",
        type: "to"
      }
    ],
    headers: {
      "Reply-To": "support-reply@clarisights.com"
    },
    important: false,
    track_opens: null,
    track_clicks: null,
    auto_text: null,
    auto_html: null,
    inline_css: null,
    url_strip_qs: null,
    preserve_recipients: null,
    view_content_link: null,
    bcc_address: "yash.arora@adwyze.com",
    tracking_domain: null,
    signing_domain: null,
    return_path_domain: null,
    merge: true,
    merge_language: "mailchimp",
    tags: ["test"]
  };
  var async = false;
  var ip_pool = "Main Pool";
  var send_at = "2015-01-01 00:00:00";
  mandrill_client.messages.send(
    { message: message, async: async, ip_pool: ip_pool, send_at: send_at },
    function(result) {
      console.log(result);
    },
    function(e) {
      console.log("A mandrill error occurred: " + e.name + " - " + e.message);
    }
  );
}
