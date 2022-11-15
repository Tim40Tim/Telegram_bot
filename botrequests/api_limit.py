from loguru import logger
from requests.structures import CaseInsensitiveDict


def limit_control(r_headers: CaseInsensitiveDict[str]) -> None:
    """Контроль бесплатного лимита запросов"""
    remaining_requests = r_headers.get("X-RateLimit-Requests-Remaining", None)
    if remaining_requests is not None:
        logger.info(f"Requests-Remaining: {remaining_requests}")
        if int(remaining_requests) <= 5:
            logger.warning(f"FEW REQUESTS REMAIN: {remaining_requests}")
    else:
        logger.error(f"No free requests: {remaining_requests}")
