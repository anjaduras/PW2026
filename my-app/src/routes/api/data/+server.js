import mysql from "mysql2/promise";

export async function GET() {
	try {
		const db = await mysql.createConnection({
			host: "localhost",
			user: "efi124",
			password: "12345",
			database: "sensor_data"
		});

		const [rows] = await db.execute(
			"SELECT * FROM measurements ORDER BY id DESC LIMIT 50"
		);

		console.log("DB rows:", rows);

		return new Response(JSON.stringify(rows.reverse()));
	} catch (err) {
		console.error("DB ERROR:", err);
		return new Response("DB ERROR");
	}
}