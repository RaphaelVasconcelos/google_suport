def test_add_firestore(operation_log, operation_log_repository):
    operation_log_repository.add(operation_log)
    operation_log_doc = operation_log_repository._collection.document(str(operation_log.uid)).get([])
    assert operation_log_doc.exists is True
