from .base_accessor import Accessor


class UserAccessor(Accessor):

    def get_user_by_email(self, email):
        def query(tx, email_val):
            res = tx.run("MATCH (u:User {email: $email}) RETURN u", email=email_val)
            first = res.single()

            if first is None:
                return None

            return first.get("u")

        with self.driver.session() as session:
            return session.read_transaction(query, email_val=email)

    def create_user(self, user):
        def query(tx, user_obj):
            return tx.run(
                """CREATE (u:User {
                    user_id: randomUuid(),
                    email: $email,
                    password: $encrypted_password,
                    name: $name
                })
                RETURN u""",
                name=user_obj.name, email=user_obj.email, encrypted_password=user_obj.encrypted_password
            ).single()

        with self.driver.session() as session:
            result = session.write_transaction(query, user)
            return result['u']
