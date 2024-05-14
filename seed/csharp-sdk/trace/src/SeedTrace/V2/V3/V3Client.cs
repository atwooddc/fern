using SeedTrace;
using SeedTrace.V2.V3;

namespace SeedTrace.V2.V3;

public class V3Client
{
    private RawClient _client;

    public V3Client(RawClient client)
    {
        _client = client;
        Problem = new ProblemClient(_client);
    }

    public ProblemClient Problem { get; }
}