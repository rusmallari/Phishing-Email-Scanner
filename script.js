async function scanEmail() {
 const email = document.getElementById("emailInput").value;
 const response = await fetch("/scan", {
   method: "POST",
   headers: {"Content-Type":"application/json"},
   body: JSON.stringify({email})
 });
 const result = await response.json();
 let html = `<h2>Risk Score: ${result.score}/100</h2><h3>${result.verdict}</h3><ul>`;
 result.reasons.forEach(r => html += `<li>${r}</li>`);
 html += "</ul>";
 document.getElementById("results").innerHTML = html;
}