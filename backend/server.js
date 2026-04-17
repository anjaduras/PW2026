import mysql from "mysql2/promise";

const db = await mysql.createConnection({
	host: "localhost",
	user: "efi124",
	password: "12345",
	database: "sensor_data"
});

export async function GET() {
	const [rows] = await db.execute(
		"SELECT * FROM measurements ORDER BY id DESC LIMIT 50"
	);

	return new Response(JSON.stringify(rows.reverse()));
}