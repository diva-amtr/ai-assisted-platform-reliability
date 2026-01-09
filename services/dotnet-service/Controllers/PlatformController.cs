using Microsoft.AspNetCore.Mvc;

[ApiController]
[Route("/")]
public class PlatformController : ControllerBase
{
    private static readonly Random Random = new();

    [HttpGet("health")]
    public IActionResult Health()
    {
        return Ok(new { status = "UP" });
    }

    [HttpGet("process")]
    public IActionResult Process()
    {
        int delay = Random.Next(300, 2000);
        Thread.Sleep(delay);

        if (Random.Next(10) < 2)
        {
            return StatusCode(500, new { error = "Simulated processing failure" });
        }

        return Ok(new
        {
            message = "Processed successfully",
            processing_time_ms = delay
        });
    }

    [HttpGet("error")]
    public IActionResult Error()
    {
        return StatusCode(500, new { error = "Intentional error triggered" });
    }
}
