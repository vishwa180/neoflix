from .base_accessor import Accessor


class FollowerAccessor(Accessor):

    def create_follow_link(self, follower_obj):
        def query(tx, followee_email, follower_email):
            return tx.run(
                """
                MATCH (follower:User {email: follower_email})
                MATCH (followee:User {email: $followee_email})
                MERGE (follower)-[r:FOLLOWS]->(followee)
                SET r.since = timestamp()
                RETURN r
                """,
                followee_email=followee_email, follower_email=follower_email
            )

        with self.driver.session() as session:
            result = session.write_transaction(query, follower_obj.followee_email, follower_obj.follower_email)
            return result['r']
