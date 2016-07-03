import time, uuid
from app import Twitter

if __name__ == '__main__':
    tw = Twitter()
    counter = 0
    _max = None
    run_id = uuid.uuid4()
    print "%s - Start time: %s" % (run_id, time.asctime())
    while counter < 1000:
        max_id, min_id = tw.fetch_all(maxid=_max)

        max_status = tw.api.get_status(max_id)
        min_status = tw.api.get_status(min_id)
        print "%s - fetched all from [%s | %s] to [%s | %s]" % (
                counter, max_id, max_status.created_at, min_id, min_status.created_at)
        _max = min_id
        counter += 1
        time.sleep(5)

        if max_id == min_id:
            break
    
    print "%s - Completion time: %s" % (run_id, time.asctime())
